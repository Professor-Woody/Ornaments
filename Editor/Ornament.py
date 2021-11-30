from Element import *
from Globals import *
from RenderEvents import *
import pygame

class Ornament(ParentElement):
    def __init__(self, ornamentId):
        ParentElement.__init__(self)
        self.id = ornamentId
        font = pygame.font.SysFont("arial", 14)
        self.image = font.render("ORNAMENT {}".format(ornamentId), 1, TEXTCOLOR)
        self.rect = self.image.get_rect()
        
        self.add(TimeBar(self, 20))
        

        
        
class TimeBar(Element):
    def __init__(self, ornament, length):
        Element.__init__(self)
        self.id = ornament.id
        
        self.image = pygame.Surface((length * 50, 20))
        self.image.fill(DARKGREY)
        self.rect = self.image.get_rect()
        self.rect.topleft = (ornament.rect.left + 200, ornament.rect.top)
        
        event = pygame.event.Event(ADDTIMEBAREVENT, sprite=self)
        pygame.event.post(event)
        
        