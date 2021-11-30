#!python
import os
from SoundFileManager import *

from RenderEvents import *
os.environ['SDL_VIDEODRIVER'] = 'windows'

import pygame
from pygame.locals import *

from Globals import *
from Panel import *
from Button import *
from Text import *
from CursorManager import *

# GUI elements
""" 
    panel
    label
    button
    waveform
    timescale
    colour picker
    animationbox
"""



class App:
    def __init__(self):
        # setup pygame
        pygame.init()
        pygame.font.init()

        # setup screen
        self.screen = pygame.display.set_mode((1200, 800), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.bg = pygame.Surface(pygame.display.get_window_size())
        self.bg.fill(BGCOLOR)
        self.screen.blit(self.bg, (0,0))

        # other
        self.keepGoing = True
        self.clock = pygame.time.Clock()


        # GUI elements
        self.gui = RenderEvents()

        self.addOptionsPanel()
        self.addMp3Panel()
        self.addOrnamentPanel()
        self.addCursorManager()
        


    def run(self):
        while self.keepGoing:
            # clear
            self.gui.clear(self.screen, self.bg)

            # events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.keepGoing = False
                elif event.type == FULLDRAWEVENT:
                    self.screen.blit(self.bg, (0,0))


            self.gui.events(events)


            # update
            self.gui.update()

            #draw
            self.gui.draw(self.screen)
            pygame.display.flip()
        
        pygame.quit()
        self.mp3Manager.quit()
    



    def addOptionsPanel(self):
        topLeftOptions = Panel((20,20), (200, 70))

        newProgramEvent = pygame.event.Event(NEWPROGRAMEVENT)
        newProgramButton = Button("NEW PROGRAM", (25, 25), 14, newProgramEvent)
        
        loadMp3Event = pygame.event.Event(LOADMP3EVENT)
        loadMp3Button = Button("LOAD MP3", (25,45), 14, loadMp3Event)
        
        saveProgramEvent = pygame.event.Event(SAVEPROGRAMEVENT)
        saveProgramButton = Button("SAVE PROGRAM", (25,65), 14, saveProgramEvent)
        

        self.gui.add(topLeftOptions)
        topLeftOptions.add(newProgramButton)
        topLeftOptions.add(loadMp3Button)
        topLeftOptions.add(saveProgramButton)


    def addMp3Panel(self):
        fileNamePanel = Panel((380, 20), (200, 50))

        self.fileNameText = Text("UNTITLED PROGRAM", (400, 25), 14)
        self.mp3NameText = Text("MP3 FILENAME", (400, 45), 14)

        fileNamePanel.add(self.fileNameText)
        fileNamePanel.add(self.mp3NameText)

        self.gui.add(fileNamePanel)


    def addOrnamentPanel(self):
        ornamentPanel = OrnamentPanel((20, 140), (200, 500))

        self.gui.add(ornamentPanel)

    def addCursorManager(self):
        cursorManager = CursorManager()
        self.gui.add(cursorManager)

if __name__ == "__main__":
    app = App()
    app.run()
    