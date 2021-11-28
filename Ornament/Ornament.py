from Light import Light
from Wifi import Wifi
from TimerHelper import TimerHelper
from Globals import *

DEBUG = False

class Ornament:
    def __init__(self):
        self.light = Light(self)
        self.wifi = Wifi() 
        self.timer = TimerHelper()
        self.keepGoing = True
        self.state = STARTING

        self.program = [] # [next_time_interval, light_state, **[args]]
        if DEBUG:
            self.state = RUNNING
            self.program = [
                (0, LIGHT_OFF),
                (500, LIGHT_ON, [WARM_WHITE]),
                (500, LIGHT_OFF),
                (500, LIGHT_ON, [WARM_WHITE]),
                (2000, LIGHT_OFF),
                (5000, RANDOM_FADE),
                (10000, PULSE, [WARM_WHITE]),
                (5000, RANDOM_FADE),
                (5000, SINGLEPULSE, [WARM_WHITE]),
                (5000, RANDOM_FADE),
                (1000, PULSE, [WARM_WHITE]),
                (0, 99)
            ]

    def run(self):
        while self.keepGoing:
            if self.state == STARTING:
                self.start()

            elif self.state == RUNNING:
                if self.timer.check():
                    nextTask = self.program.pop(0)
                    nextTime = nextTask[0]
                    task = nextTask[1]
                    args = []
                    if len(nextTask) == 3:
                        args = nextTask[2]

                    if task == PROGRAM_END:
                        self.state = STOPPED

                    elif task == PROGRAM_FETCH:
                        self.state = STARTING

                    else:
                        self.timer.set(nextTime)
                        self.light.setTask(task, args)
                self.light.update()
                self.light.draw()
            
    def start(self):
        self.program = self.wifi.getProgram()["prog"]
        self.state = RUNNING


                        
