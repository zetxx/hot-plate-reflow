from lib.ST7735 import TFT
from lib.sysfont import sysfont
from machine import SPI,Pin
import time
import math
# no use GPIOs 12, 0, 2, 4, 15, 5 (0,2, and 12)
# SCK(CLK,SCL)    IO 14    IO 32
# SDA(MOSI)       IO 13    IO 27
# RST(RES)        IO 17    IO 26
# A0(DC)          IO 16    IO 25
# CS              IO 18    IO 33
# !miso           IO 12    IO 35
# 
#
displaySize = [160, 128] # [x, y]
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(32), mosi=Pin(27), miso=Pin(35))
tft=TFT(spi,25,26,33)
tft.initb2()
tft.rgb(True)
tft.rotation(3)
tft.rotation(1)
tft.fill(TFT.BLACK)

# 128x160
def info(on = False, hover = False, temp = 0):
    bgColor = TFT.color(0, 0, 255)
    tempColor = TFT.color(255, 255, 255)
    text = 'START'
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
    marginBottom = 8
    marginLeft = 156
    tempColor = TFT.color(255, 169, 169)
    timeColor = TFT.color(255, 255, 255)
    tft.line([displaySize[0] - marginLeft, displaySize[1] - 108], [displaySize[0] - marginLeft, displaySize[1]], tempColor)
    tft.line([displaySize[0] - 160, displaySize[1] - marginBottom], [displaySize[0], displaySize[1] - marginBottom], timeColor)
    tft.text((0, 22), 'c', tempColor, sysfont, 1, nowrap=True)
    tft.text((154, 120), 't', timeColor, sysfont, 1, nowrap=True)
    sumTi, sumTe = sumTT(stages)
    x1 = displaySize[0] - marginLeft
    y1 = displaySize[1] - marginBottom
    ti = (displaySize[0] - marginBottom) / sumTi
    te = (displaySize[1] - 28) / sumTe
    z = [TFT.color(0, 255, 0), TFT.color(0, 0, 255), TFT.color(255, 0, 0)]
    for i in range(0, len(stages)):
        time, temp = stages[i]
        x2 = x1 + math.floor(ti * time)
        y2 = y1 - math.floor(te * temp)
        tft.line((x1, y1), (x2, y2), z[i])
        tft.text((((x2 - x1) / 2) + x1, ((y2 - y1) / 2) + y1), str(time), timeColor, sysfont)
        tft.text((((x2 - x1) / 2) + x1, (((y2 - y1) / 2) + y1) - 10), str(temp), tempColor, sysfont)
        x1, y1 = x2, y2

def init():
    info(on = False, hover = False, temp = 320)
    graph(stages = [[120, 80], [140, 180], [90, 245]])
