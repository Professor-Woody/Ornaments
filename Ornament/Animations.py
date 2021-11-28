from Globals import *
from TimerHelper import *


class AnimationSequence:
    def __init__(self, args):
        self.hasChanged = True
        self.index = 0
        self.color = COLOR_LIST[0]


    def update(self):
        pass


    def getColor(self):
        self.hasChanged = False
        return self.color


    def getNextColor(self):
        color = COLOR_LIST[self.index]
        self.index += 1
        if self.index >= len(COLOR_LIST)-1:
            self.index = 0
        return color


    def setColor(self, color):
        self.hasChanged = True
        self.color = color

    
    def calculateDeltas(self, currentColor, targetColor):
        deltaR = targetColor[0] - currentColor[0]
        deltaG = targetColor[1] - currentColor[1]
        deltaB = targetColor[2] - currentColor[2]
        return (deltaR, deltaG, deltaB)



class RandomBlink(AnimationSequence):
    def __init__(self, args):
        AnimationSequence.__init__(self, args)
        self.timer = TimerHelper()
        self.timer.set(BLINK_SPEED)


    def update(self):
        if self.timer.check():
            self.timer.set(BLINK_SPEED)
            self.setColor(self.getNextColor())





class RandomFade(AnimationSequence):
    def __init__(self, args):
        AnimationSequence.__init__(self, args)
        self.deltaR = 0
        self.deltaG = 0
        self.deltaB = 0
        self.ratio = 0

        self.timer = TimerHelper()
        self.timer.setFPS(10)

        self.color = args[0]

    def update(self):
        if self.timer.checkFPS():
            if self.ratio <= 0.0:
                self.ratio = 1.0
                self.chosenColor = self.getNextColor()
                self.deltaR, self.deltaG, self.deltaB = self.calculateDeltas(self.color, self.chosenColor)
            
            color = [0,0,0]
            color[0] = int(self.chosenColor[0] - (self.deltaR * self.ratio))
            color[1] = int(self.chosenColor[1] - (self.deltaG * self.ratio))
            color[2] = int(self.chosenColor[2] - (self.deltaB * self.ratio))
            self.setColor(color)
            self.ratio -= .01
 




class SinglePulse(AnimationSequence):
    RISING = 0
    FALLING = 1
    STOPPED = 2
    RISINGSPEED = .1
    FALLINGSPEED = .005
    def __init__(self, args):
        AnimationSequence.__init__(self, args)
        self.ratio = 1.0

        self.timer = TimerHelper()
        self.timer.setFPS(100)

        self.chosenColor = list(args[0])
        self.color = list(args[1])
        self.deltaR, self.deltaG, self.deltaB = self.calculateDeltas(self.color, self.chosenColor)

        self.state = self.RISING
        self.deltaSpeed = self.RISINGSPEED

    def update(self):
        if self.state == self.STOPPED: 
            return

        if self.timer.checkFPS():
            if self.state == self.RISING:
                if self.ratio <= 0.0:
                    self.state = self.FALLING
                    self.chosenColor = [int(x*.05) for x in self.chosenColor]
                    self.deltaR, self.deltaG, self.deltaB = self.calculateDeltas(self.color, self.chosenColor)
                    self.ratio = 1.0

            elif self.state == self.FALLING:
                if self.ratio <= 0.0:
                    self.state = self.STOPPED

            color = [0,0,0]
            color[0] = int(self.chosenColor[0] - (self.deltaR * self.ratio))
            color[1] = int(self.chosenColor[1] - (self.deltaG * self.ratio))
            color[2] = int(self.chosenColor[2] - (self.deltaB * self.ratio))
            self.setColor(color)

            self.ratio -= self.deltaSpeed




        


class Pulse(AnimationSequence):
    RISING = 0
    FALLING = 1
    RISINGSPEED = .1
    FALLINGSPEED = .005
    def __init__(self, args):
        AnimationSequence.__init__(self, args)
        self.ratio = 1.0

        self.timer = TimerHelper()
        self.timer.setFPS(100)

        self.topColor = list(args[0])
        self.bottomColor = [int(x*.05) for x in self.topColor]
        self.targetColor = self.topColor

        self.color = list(args[1])
        self.deltaR, self.deltaG, self.deltaB = self.calculateDeltas(self.color, self.topColor)

        self.state = self.RISING
        self.deltaSpeed = self.RISINGSPEED


    def update(self):
        if self.timer.checkFPS():
            if self.state == self.RISING:
                if self.ratio <= 0.0:
                    self.state = self.FALLING
                    self.deltaR, self.deltaG, self.deltaB = self.calculateDeltas(self.color, self.bottomColor)
                    self.targetColor = self.bottomColor
                    self.ratio = 1.0
                    self.deltaSpeed = self.FALLINGSPEED

            elif self.state == self.FALLING:
                if self.ratio <= 0.0:
                    self.state = self.RISING
                    self.deltaR, self.deltaG, self.deltaB = self.calculateDeltas(self.color, self.topColor)
                    self.targetColor = self.topColor
                    self.ratio = 1.0
                    self.deltaSpeed = self.RISINGSPEED

            color = [0,0,0]
            color[0] = int(self.targetColor[0] - (self.deltaR * self.ratio))
            color[1] = int(self.targetColor[1] - (self.deltaG * self.ratio))
            color[2] = int(self.targetColor[2] - (self.deltaB * self.ratio))
            self.setColor(color)

            self.ratio -= self.deltaSpeed






class LightOff(AnimationSequence):
    def __init__(self, args):
        AnimationSequence.__init__(self, args)
        self.setColor(BLACK)


class LightOn(AnimationSequence):
    def __init__(self, args):
        AnimationSequence.__init__(self, args)
        self.setColor(args[0])


class SingleColorBlink(AnimationSequence):
    def __init__(self, args):
        AnimationSequence.__init__(self, args)
        self.setColor(args[0])
        self.colors = {True: args[0], False: BLACK}
        self.timer = TimerHelper()
        self.timer.set(BLINK_SPEED)
        self.on = True
    
    def update(self):
        if self.timer.check():
            self.timer.set(BLINK_SPEED)
            self.on = not self.on
            self.setColor(self.colors[self.on])


        

    
    