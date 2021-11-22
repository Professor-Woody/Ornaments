import machine, neopixel
from TimerHelper import *
import random

LIGHT_OFF = 0
LIGHT_ON = 1
RANDOM_FADE = 2
SINGLEPULSE = 3
PULSE = 4
RANDOM_BLINK = 5


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WARM_WHITE = (255, 255, 75)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

COLOR_LIST = [RED, GREEN, BLUE, PURPLE, YELLOW, CYAN]

BLINK_SPEED = 1500
COLOR_STEP_AMOUNT = 1

class Light:
    def __init__(self, parent):
        self.parent = parent
        self.pixels = neopixel.NeoPixel(machine.Pin(4, machine.Pin.OUT), 1)
        self.timer = TimerHelper()
        self.timer.setFPS(10)
        self.hasChanged = False

        self.currentColor = BLACK
        self.chosenColor = WHITE
        self.index = 0

    def update(self):
        if self.state == RANDOM_BLINK:
            if self.timer.check():
                self.timer.set(BLINK_SPEED)
                self.setColor(self.getNextColor())


        elif self.state == RANDOM_FADE:
            if self.timer.checkFPS():                
                if self.currentColor == self.chosenColor:
                    self.currentColor = self.getNextColor()
                
                r, g, b = self.currentColor
                newR, newG, newB = self.chosenColor
                r = self.fadeColor(r, newR)
                g = self.fadeColor(g, newG)
                b = self.fadeColor(b, newB)
                self.currentColor = (r, g, b)
                self.setColor(self.currentColor)


    def getNextColor(self):
        color = COLOR_LIST[self.index]
        self.index += 1
        if self.index >= len(COLOR_LIST)-1:
            self.index = 0
        return color

        
    def fadeColor(self, a, newA):
        if a - newA > COLOR_STEP_AMOUNT or a - newA < COLOR_STEP_AMOUNT:
            if a < newA:
                a += COLOR_STEP_AMOUNT
            else:
                a -= COLOR_STEP_AMOUNT
        else:
            a = newA
        return a



    def setTask(self, task):
        self.state = task
        if task == LIGHT_OFF:
            self.setColor(BLACK)
        elif task == LIGHT_ON:
            self.setColor(WHITE)
        elif task == RANDOM_BLINK:
            self.timer.set(BLINK_SPEED)


    def setColor(self, color):
        self.hasChanged = True
        self.pixels[0] = color

    def draw(self):
        if self.hasChanged:
            self.pixels.write()
            self.hasChanged = False
