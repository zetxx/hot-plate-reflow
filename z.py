from time import sleep
from ssd1351 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont
import math

spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(17), cs=Pin(5), rst=Pin(16))
display.contrast(15)
display.clear()


ffont = XglcdFont('fonts/FixedFont5x8.c', 5, 8)
font = XglcdFont('fonts/Unispace12x24.c', 12, 24)

def info(on = False, hover = False, temp = 0):
    bgColor = color565(0, 0, 255)
    tempColor = color565(255, 255, 255)
    text = 'START'

    if on:
        bgColor = color565(255, 0, 0)
        text = 'STOP'

    if not on and temp > 38:
        tempColor = color565(255, 0, 0)

    textBgColor = bgColor
    if hover == True:
        textBgColor = color565(0, 0, 0)

    display.fill_hrect(0, 0, 128, 32, bgColor)
    display.draw_text(5, 5, text, font, color565(255, 255, 255), background=textBgColor)
    display.draw_text(80, 5, str(temp), font, tempColor, background=bgColor)

def sumTT(tt):
    time, temp = [0, 0]
    for i in range(0, len(tt)):
        ti, te = tt[i]
        time = time + ti
        temp = temp + te
    return [time, temp]

def graph():
    # items of items of time, temp
    stages = [[100, 40], [30, 200], [120, 210]]
    tempColor = color565(255, 169, 169)
    timeColor = color565(255, 255, 255)
    display.draw_vline(7, 40, 88, tempColor)
    display.draw_hline(0, 118, 120, timeColor)
    display.draw_text(0, 44, 'c', ffont, tempColor)
    display.draw_text(110, 120, 't', ffont, timeColor)
    sumTi, sumTe = sumTT(stages)
    ti = 112 / sumTi
    te = 68 / sumTe
    x1 = 8
    y1 = 118
    z = [color565(255, 0, 0), color565(0, 255, 0), color565(0, 0, 255)]
    for i in range(0, len(stages)):
        time, temp = stages[i]
        x2 = x1 + math.floor(ti * time)
        y2 = y1 - math.floor(te * temp)
        display.draw_line(x1, y1, x2, y2, z[i])
        display.draw_text(x1 + math.floor((x2 - x1) / 2), y2 - 16, str(time), ffont, timeColor)
        display.draw_text(x1 + math.floor((x2 - x1) / 2), y2 - 7, str(temp), ffont, tempColor)
        # print('----------------------------')
        # print('x1, y1', [x1, y1])
        # print('x2, y2', [x2, y2])
        # print('----------------------------')
        x1, y1 = x2, y2
    display.contrast(15)

def run():
    info(on = True, hover = True, temp = 320)
    graph()

run()