from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import math
# SCK(CLK,SCL)    IO 14    IO 15
# SDA(MOSI)       IO 13    IO 02.
# RST(RES)        IO 17    IO 04.
# A0(DC)          IO 16    IO 05.
# CS              IO 18    IO 13.
# !miso           IO 12    IO 35
# 
# 
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(15), mosi=Pin(2), miso=Pin(35))
tft=TFT(spi,5,4,13)
tft.initb2()
tft.rgb(True)
tft.rotation(3)
tft.fill(TFT.BLACK)

# 128x160
def info(on = False, hover = False, temp = 0):
    bgColor = TFT.color(0, 0, 255)
    tempColor = TFT.color(255, 255, 255)
    text = 'START'
    print(bgColor)
    if on:
        bgColor = TFT.color(255, 0, 0)
        text = 'STOP'

    if not on and temp > 38:
        tempColor = TFT.color(255, 0, 0)

    textBgColor = bgColor
    if hover == True:
        textBgColor = TFT.color(50, 50, 50)
    #             x,y       w.h
    tft.fillrect((0, 0), (160, 20), bgColor)
    tft.fillrect((0, 0), (80, 20), textBgColor)
    #          x, y
    tft.text((5, 6), text, TFT.color(255, 255, 255), sysfont, 1, nowrap=True)
    tft.text((100, 4), str(temp), tempColor, sysfont, 2, nowrap=True)

# def sumTT(tt):
#     time, temp = [0, 0]
#     for i in range(0, len(tt)):
#         ti, te = tt[i]
#         time = time + ti
#         temp = temp + te
#     return [time, temp]

def graph():
#     # items of items of time, temp
    stages = [[100, 40], [30, 200], [120, 210]]
    tempColor = TFT.color(255, 169, 169)
    timeColor = TFT.color(255, 255, 255)
#     display.draw_vline(7, 40, 88, tempColor)
#     display.draw_hline(0, 118, 120, timeColor)
#     display.draw_text(0, 44, 'c', ffont, tempColor)
#     display.draw_text(110, 120, 't', ffont, timeColor)
#     sumTi, sumTe = sumTT(stages)
#     ti = 112 / sumTi
#     te = 68 / sumTe
#     x1 = 8
#     y1 = 118
    # z = [TFT.color(255, 0, 0), TFT.color(0, 255, 0), TFT.color(0, 0, 255)]
#     for i in range(0, len(stages)):
#         time, temp = stages[i]
#         x2 = x1 + math.floor(ti * time)
#         y2 = y1 - math.floor(te * temp)
#         display.draw_line(x1, y1, x2, y2, z[i])
#         display.draw_text(x1 + math.floor((x2 - x1) / 2), y2 - 16, str(time), ffont, timeColor)
#         display.draw_text(x1 + math.floor((x2 - x1) / 2), y2 - 7, str(temp), ffont, tempColor)
#         # print('----------------------------')
#         # print('x1, y1', [x1, y1])
#         # print('x2, y2', [x2, y2])
#         # print('----------------------------')
#         x1, y1 = x2, y2
#     display.contrast(15)

def run():
    info(on = False, hover = False, temp = 320)
    graph()

run()