# https://github.com/miketeachman/micropython-rotary
# https://www.keebtalk.com/t/how-to-wire-a-rotary-encoder-fit-in-a-matrix/6330

import time
from lib.rotary_irq_esp import RotaryIRQ
from lib.button import debouncer

r = RotaryIRQ(pin_num_clk=13,
              pin_num_dt=14,
              reverse=True)
def rotaryPrint():
    print(r.value())

def run(cb):
    r.add_listener(lambda: cb('rotary', r.value()))
    debouncer(15, cb=lambda:cb('button', 1))