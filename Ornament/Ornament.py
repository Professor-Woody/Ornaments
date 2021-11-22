""" Ornament
    The ornaments are ESP8266's
    They connect to a web server
        get time
        get ID
        get program
        parse program
    At appropriate start time
        start program
        run through commands

"""

import json
from Light import Light
from Wifi import Wifi
from TimerHelper import TimerHelper

STARTING = 0
CONNECT = 1
RUNNING = 2
STOPPED = 3

PROGRAM_FETCH = 98
PROGRAM_END = 99

class Ornament:
    def __init__(self):
        self.light = Light(self)
        self.wifi = Wifi() # all connection will 
        self.timer = TimerHelper()
        self.keepGoing = True
        self.state = STARTING

        self.program = [] # [next_time_interval, light_state]

    def run(self):
        while self.keepGoing:
            if self.state == STARTING:
                self.start()

            elif self.state == RUNNING:
                if self.timer.check():
                    nextTime, task = self.program.pop(0)
                    if task == PROGRAM_END:
                        self.state == STOPPED

                    elif task == PROGRAM_FETCH:
                        self.state = STARTING

                    else:
                        self.timer.set(nextTime)
                        self.light.setTask(task)
                self.light.update()
                self.light.draw()
            
    def start(self):
        self.program = self.wifi.getProgram()["prog"]
        self.state = RUNNING


                        
