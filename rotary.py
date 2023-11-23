# https://github.com/miketeachman/micropython-rotary
# https://www.keebtalk.com/t/how-to-wire-a-rotary-encoder-fit-in-a-matrix/6330

import time
from machine import Pin
from lib.rotary_irq_esp import RotaryIRQ
from lib.button import Button

r = RotaryIRQ(pin_num_clk=13,
              pin_num_dt=14,
              reverse=True)
def rotaryPrint():
    print('rotary')
    print(r.value())

r.add_listener(rotaryPrint)
Button(pinnum=15, callback=lambda p:print(time.time()))
