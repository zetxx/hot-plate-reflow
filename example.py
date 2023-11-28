"""
hello.py

    Writes "Hello!" in random colors at random locations on the display.
"""

import random
import utime
import st7789
import tft_config
import vga2_8x8 as font
import romanp as v_font

tft = tft_config.config(1)
tft.init()
tft.fill(st7789.BLACK)
tft.hline(159, 127, 1, st7789.WHITE)
# x(1-159) y(1-127)
fixDim = [[1, 159], [1, 127]]
tft.text(font, '300', 20, 20, st7789.WHITE, st7789.RED)
tft.draw(v_font, '300', 40, 40, st7789.WHITE, 0.8)
