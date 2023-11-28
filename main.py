import rotary
import screen

state = {
    'heating': False,
    'screen': 'Main'
}
def rotaryButtonCb(t, value):
    print(t, value)
rotary.run(rotaryButtonCb)
screen.init()
