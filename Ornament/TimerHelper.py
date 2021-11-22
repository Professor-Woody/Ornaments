import time


class TimerHelper:
    def __init__(self):
        self.targetTime = 0
        pass

    def set(self, timeInMS):
        self.targetTime = time.ticks_ms() + timeInMS

    def setFPS(self, FPS):
        self.FPS = FPS

    def check(self):
        if time.ticks_ms() >= self.targetTime:
            return True
        return False

    def checkFPS(self):
        currentTime = time.ticks_ms()
        if currentTime > self.targetTime:
            self.targetTime = currentTime + (1000.0 / self.FPS)
            return True
        return False
