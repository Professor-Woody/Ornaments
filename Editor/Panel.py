import pygame
from Element import *
from Globals import *
from RenderEvents import *
from Button import *
from Ornament import *

class Panel(ParentElement):
    def __init__(self, position, size):
        ParentElement.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(DARKGREY)

        self.rect = self.image.get_rect()
        self.move(position)



class OrnamentPanel(Panel):
    def __init__(self, position, size):
        Panel.__init__(self, position, size)
        addOrnamentEvent = pygame.event.Event(NEWORNAMENTEVENT)
        self.addOrnamentButton = Button("(+)", 
                                        (0,0), 
                                        14, 
                                        addOrnamentEvent)
        self.addSprite(self.addOrnamentButton)

        self.ornamentIndex = 0

    def events(self, events):
        Panel.events(self, events)
        for evt in events:
            if evt.type == NEWORNAMENTEVENT:
                ornament = Ornament(self.ornamentIndex)
                self.add(ornament)
                self.ornamentIndex += 1
                
    def add(self, sprite):
        self.children.remove(self.addOrnamentButton)
        self.addSprite(sprite)
        self.reAddButton()
        
    def reAddButton(self):
        self.addOrnamentButton.amove((0,0))
        self.addSprite(self.addOrnamentButton)        

    def addSprite(self, sprite):
        index = len(self.children) * 30
        x = self.rect.x + 5
        y = self.rect.y + 5 + index
        sprite.move((x,y))
        self.children.add(sprite)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.children.draw(screen)
