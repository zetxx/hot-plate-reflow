"""Generic ESP32 with 128x160 7735 display"""

from machine import Pin, SPI
import st7789

# no use GPIOs 12, 0, 2, 4, 15, 5 (0,2, and 12)
# SCK(CLK,SCL)    IO 14    IO 32
# SDA(MOSI)       IO 13    IO 27
# RST(RES)        IO 17    IO 26
# A0(DC)          IO 16    IO 25
# CS              IO 18    IO 33
# !miso           IO 12    IO 35

TFA = 0
BFA = 0

def config(rotation=0, buffer_size=0, options=0):
    return st7789.ST7789(
        SPI(1, baudrate=20000000, sck=Pin(32), mosi=Pin(27)),
        128,
        160,
        reset=Pin(26, Pin.OUT),
        cs=Pin(33, Pin.OUT),
        dc=Pin(25, Pin.OUT),
        color_order=st7789.RGB,
        inversion=False,
        rotation=rotation,
        options=options,
        buffer_size=buffer_size)