import pygame

from RenderEvents import *
from Text import *


class CursorManager(Text):
    def __init__(self):
        w, h = pygame.display.get_surface().get_size()
        self.text = "nothing"
        Text.__init__(self, self.text, (20, h - 40), 14)
        self.timeBars = RenderEvents()
        
        
    def events(self, events):
        text = ""
        pos = ""
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                pos = str(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    text = "Mouse Down"
                    pos = str(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                if not pygame.mouse.get_pressed()[0]:
                    text = "Mouse Up"
                    pos = str(pygame.mouse.get_pos())
            elif event.type == ADDTIMEBAREVENT:
                print ("adding timeBar")
                self.timeBars.add(event.sprite)
        
        if text or pos:
            if not text:
                text = self.text
            else:
                self.text = text
            text += " | {}".format(pos)
            self.setText(text)    
            