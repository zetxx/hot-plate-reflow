# https://github.com/miketeachman/micropython-rotary

import time
from lib.rotary_irq_esp import RotaryIRQ

r = RotaryIRQ(pin_num_clk=12, 
              pin_num_dt=13, 
              min_val=0, 
              max_val=5, 
              reverse=False, 
              range_mode=RotaryIRQ.RANGE_UNBOUNDED)
              
val_old = r.value()
while True:
    val_new = r.value()
    
    if val_old != val_new:
        val_old = val_new
        print('result =', val_new)
        
    time.sleep_ms(50)