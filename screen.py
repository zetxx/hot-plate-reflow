import st7789
import tft_config
from machine import SPI,Pin
import time
import math
import vga2_8x8 as font
import romanp as v_font

# no use GPIOs 12, 0, 2, 4, 15, 5 (0,2, and 12)
# SCK(CLK,SCL)    IO 14    IO 32
# SDA(MOSI)       IO 13    IO 27
# RST(RES)        IO 17    IO 26
# A0(DC)          IO 16    IO 25
# CS              IO 18    IO 33
# !miso           IO 12    IO 35
# 
#
# https://github.com/russhughes/st7789_mpy/tree/master
displaySize = [159, 127] # [x, y]
tft = tft_config.config(1) # top,left
tft.init()
tft.fill(st7789.BLACK)
def info(on = False, hover = False, temp = 0):
    bgColor = st7789.color565(0, 0, 255)
    tempColor = st7789.color565(255, 255, 255)
    text = 'START'
    if on:
        bgColor = st7789.color565(255, 0, 0)
        text = 'STOP'

    if not on and temp > 38:
        tempColor = st7789.color565(255, 0, 0)

    textBgColor = bgColor
    if hover == True:
        textBgColor = st7789.color565(50, 50, 50)

    tft.fill_rect(1, 1, 78, 25, textBgColor)
    tft.fill_rect(80, 1, 77, 25, bgColor)
    tft.draw(v_font, text, 10, 12, st7789.color565(255, 255, 255), 1.2)
    tft.draw(v_font, str(temp), 110, 12, tempColor, 1.2)

def sumTT(tt):
    time, temp = [0, 0]
    for i in range(0, len(tt)):
        ti, te = tt[i]
        time = time + ti
        temp = temp + te
    return [time, temp]
# [[time, temperature], [time, temperature], [time, temperature]]
def graph(stages = [[100, 40], [60, 200], [120, 210]]):
    # items of items of time, temp
    margin = 7
    timeColor = st7789.color565(255, 255, 255)
    tft.hline(1, displaySize[1] - margin, 160, timeColor)
    tempColor = st7789.RED
    tft.vline(margin, 35, 90, tempColor)
    tft.text(font, 'c', 1, 37, tempColor)
    tft.text(font, 't', 150, 120, timeColor)
    sumTi, sumTe = sumTT(stages)
    x1 = margin
    y1 = displaySize[1] - margin
    ti = (displaySize[0] - margin) / sumTi
    te = (displaySize[1]  - 30 - margin) / sumTe
    z = [st7789.GREEN, st7789.MAGENTA, st7789.color565(0, 0, 255)]
    for i in range(0, len(stages)):
        print(x1, y1)
        time, temp = stages[i]
        x2 = x1 + math.floor(ti * time)
        y2 = y1 - math.floor(te * temp)
        tft.line(x1, y1, x2, y2, z[i])
#         tft.text((((x2 - x1) / 2) + x1, ((y2 - y1) / 2) + y1), str(time), timeColor, sysfont)
#         tft.text((((x2 - x1) / 2) + x1, (((y2 - y1) / 2) + y1) - 10), str(temp), tempColor, sysfont)
        x1, y1 = x2, y2

def init():
    info(on = True, hover = True, temp = 320)
    graph(stages = [[20, 80], [140, 180], [90, 245]])
