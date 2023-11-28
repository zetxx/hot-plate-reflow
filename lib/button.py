import time
from machine import Pin, Timer

timer = Timer(0)

def debounce(cb):
    def _debounce(pin):
        timer.init(mode=Timer.ONE_SHOT, period=200, callback=cb)
    return _debounce

def debouncer(pin, cb):
    button = Pin(pin, Pin.IN, Pin.PULL_UP)
    button.irq(debounce(cb), Pin.IRQ_RISING)