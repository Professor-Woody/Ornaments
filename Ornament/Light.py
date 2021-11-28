import machine, neopixel
from TimerHelper import *
from Animations import *
from Globals import *

animations = {
    RANDOM_BLINK: RandomBlink, 
    LIGHT_OFF: LightOff, 
    LIGHT_ON: LightOn, 
    RANDOM_FADE: RandomFade,
    SINGLEPULSE: SinglePulse,
    PULSE: Pulse,
    SINGLECOLORBLINK: SingleColorBlink
    }

class Light:
    def __init__(self, parent):
        self.parent = parent
        self.pixels = neopixel.NeoPixel(machine.Pin(4, machine.Pin.OUT), 1)
        self.hasChanged = False
        self.currentColor = BLACK

        self.animation = RandomBlink([])

    def update(self):
        self.animation.update()
        if self.animation.hasChanged:
            self.setColor(self.animation.getColor())

    def setTask(self, task, args):
        args.append(self.currentColor)
        self.animation = animations[task](args)


    def setColor(self, color):
        self.hasChanged = True
        self.currentColor = color
        self.pixels[0] = color
        

    def draw(self):
        if self.hasChanged:
            self.pixels.write()
            self.hasChanged = False




