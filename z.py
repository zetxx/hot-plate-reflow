from ST7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import math
# SCK(CLK)    IO 14    IO 18
# SDA(MOSI)   IO 13    IO 23
# RST(RES)    IO 17    IO 04
# A0(DC)      IO 16    IO 02
# CS          IO 18    IO 15
# 
# 
# 
spi = SPI(2, baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(12))
tft=TFT(spi,2,4,15)
tft.initr()
tft.rgb(True)

def testlines(color):
    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((0,0),(x, tft.size()[1] - 1), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((0,0),(tft.size()[0] - 1, y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((tft.size()[0] - 1, 0), (x, tft.size()[1] - 1), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((tft.size()[0] - 1, 0), (0, y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((0, tft.size()[1] - 1), (x, 0), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((0, tft.size()[1] - 1), (tft.size()[0] - 1,y), color)

    tft.fill(TFT.BLACK)
    for x in range(0, tft.size()[0], 6):
        tft.line((tft.size()[0] - 1, tft.size()[1] - 1), (x, 0), color)
    for y in range(0, tft.size()[1], 6):
        tft.line((tft.size()[0] - 1, tft.size()[1] - 1), (0, y), color)

def testfastlines(color1, color2):
    tft.fill(TFT.BLACK)
    for y in range(0, tft.size()[1], 5):
        tft.hline((0,y), tft.size()[0], color1)
    for x in range(0, tft.size()[0], 5):
        tft.vline((x,0), tft.size()[1], color2)

def testdrawrects(color):
    tft.fill(TFT.BLACK);
    for x in range(0,tft.size()[0],6):
        tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color)

def testfillrects(color1, color2):
    tft.fill(TFT.BLACK);
    for x in range(tft.size()[0],0,-6):
        tft.fillrect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color1)
        tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), color2)


def testfillcircles(radius, color):
    for x in range(radius, tft.size()[0], radius * 2):
        for y in range(radius, tft.size()[1], radius * 2):
            tft.fillcircle((x, y), radius, color)

def testdrawcircles(radius, color):
    for x in range(0, tft.size()[0] + radius, radius * 2):
        for y in range(0, tft.size()[1] + radius, radius * 2):
            tft.circle((x, y), radius, color)

def testtriangles():
    tft.fill(TFT.BLACK);
    color = 0xF800
    w = tft.size()[0] // 2
    x = tft.size()[1] - 1
    y = 0
    z = tft.size()[0]
    for t in range(0, 15):
        tft.line((w, y), (y, x), color)
        tft.line((y, x), (z, x), color)
        tft.line((z, x), (w, y), color)
        x -= 4
        y += 4
        z -= 4
        color += 100

def testroundrects():
    tft.fill(TFT.BLACK);
    color = 100
    for t in range(5):
        x = 0
        y = 0
        w = tft.size()[0] - 2
        h = tft.size()[1] - 2
        for i in range(17):
            tft.rect((x, y), (w, h), color)
            x += 2
            y += 3
            w -= 4
            h -= 6
            color += 1100
        color += 100

def tftprinttest():
    tft.fill(TFT.BLACK);
    v = 30
    tft.text((0, v), "Hello World!", TFT.RED, sysfont, 1, nowrap=True)
    v += sysfont["Height"]
    tft.text((0, v), "Hello World!", TFT.YELLOW, sysfont, 2, nowrap=True)
    v += sysfont["Height"] * 2
    tft.text((0, v), "Hello World!", TFT.GREEN, sysfont, 3, nowrap=True)
    v += sysfont["Height"] * 3
    tft.text((0, v), str(1234.567), TFT.BLUE, sysfont, 4, nowrap=True)
    time.sleep_ms(1500)
    tft.fill(TFT.BLACK);
    v = 0
    tft.text((0, v), "Hello World!", TFT.RED, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), str(math.pi), TFT.GREEN, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), " Want pi?", TFT.GREEN, sysfont)
    v += sysfont["Height"] * 2
    tft.text((0, v), hex(8675309), TFT.GREEN, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), " Print HEX!", TFT.GREEN, sysfont)
    v += sysfont["Height"] * 2
    tft.text((0, v), "Sketch has been", TFT.WHITE, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), "running for: ", TFT.WHITE, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), str(time.ticks_ms() / 1000), TFT.PURPLE, sysfont)
    v += sysfont["Height"]
    tft.text((0, v), " seconds.", TFT.WHITE, sysfont)

def test_main():
    tft.fill(TFT.BLACK)
    tft.text((0, 0), "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur adipiscing ante sed nibh tincidunt feugiat. Maecenas enim massa, fringilla sed malesuada et, malesuada sit amet turpis. Sed porttitor neque ut ante pretium vitae malesuada nunc bibendum. Nullam aliquet ultrices massa eu hendrerit. Ut sed nisi lorem. In vestibulum purus a tortor imperdiet posuere. ", TFT.WHITE, sysfont, 1)
    time.sleep_ms(1000)

    tftprinttest()
    time.sleep_ms(4000)

    testlines(TFT.YELLOW)
    time.sleep_ms(500)

    testfastlines(TFT.RED, TFT.BLUE)
    time.sleep_ms(500)

    testdrawrects(TFT.GREEN)
    time.sleep_ms(500)

    testfillrects(TFT.YELLOW, TFT.PURPLE)
    time.sleep_ms(500)

    tft.fill(TFT.BLACK)
    testfillcircles(10, TFT.BLUE)
    testdrawcircles(10, TFT.WHITE)
    time.sleep_ms(500)

    testroundrects()
    time.sleep_ms(500)

    testtriangles()
    time.sleep_ms(500)

test_main()
# from time import sleep
# from ssd1351 import Display, color565
# from machine import Pin, SPI
# from xglcd_font import XglcdFont
# import math

# spi = SPI(2, baudrate=14500000, sck=Pin(18), mosi=Pin(23))
# display = Display(spi, dc=Pin(17), cs=Pin(5), rst=Pin(16))
# display.contrast(15)
# display.clear()


# ffont = XglcdFont('fonts/FixedFont5x8.c', 5, 8)
# font = XglcdFont('fonts/Unispace12x24.c', 12, 24)

# def info(on = False, hover = False, temp = 0):
#     bgColor = color565(0, 0, 255)
#     tempColor = color565(255, 255, 255)
#     text = 'START'

#     if on:
#         bgColor = color565(255, 0, 0)
#         text = 'STOP'

#     if not on and temp > 38:
#         tempColor = color565(255, 0, 0)

#     textBgColor = bgColor
#     if hover == True:
#         textBgColor = color565(0, 0, 0)

#     display.fill_hrect(0, 0, 128, 32, bgColor)
#     display.draw_text(5, 5, text, font, color565(255, 255, 255), background=textBgColor)
#     display.draw_text(80, 5, str(temp), font, tempColor, background=bgColor)

# def sumTT(tt):
#     time, temp = [0, 0]
#     for i in range(0, len(tt)):
#         ti, te = tt[i]
#         time = time + ti
#         temp = temp + te
#     return [time, temp]

# def graph():
#     # items of items of time, temp
#     stages = [[100, 40], [30, 200], [120, 210]]
#     tempColor = color565(255, 169, 169)
#     timeColor = color565(255, 255, 255)
#     display.draw_vline(7, 40, 88, tempColor)
#     display.draw_hline(0, 118, 120, timeColor)
#     display.draw_text(0, 44, 'c', ffont, tempColor)
#     display.draw_text(110, 120, 't', ffont, timeColor)
#     sumTi, sumTe = sumTT(stages)
#     ti = 112 / sumTi
#     te = 68 / sumTe
#     x1 = 8
#     y1 = 118
#     z = [color565(255, 0, 0), color565(0, 255, 0), color565(0, 0, 255)]
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

# def run():
#     info(on = True, hover = True, temp = 320)
#     graph()

# run()