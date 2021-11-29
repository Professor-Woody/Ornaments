import pygame
from Element import *
from Globals import *
from RenderEvents import *
from Button import *
from Ornament import *

class Panel(Element):
    def __init__(self, position, size):
        Element.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(DARKGREY)

        self.rect = self.image.get_rect()
        self.rect.move_ip(position)

        self.children = RenderEvents()

    def add(self, sprite):
        self.children.add(sprite)

    def remove(self, sprite):
        self.children.remove(sprite)


    def events(self, events):
        self.children.events(events)

    def update(self):
        self.children.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.children.draw(screen)




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
        self.addSprite(self.addOrnamentButton)

    def addSprite(self, sprite):
        index = len(self.children) * 30
        x = self.rect.x + 5
        y = self.rect.y + 5 + index
        sprite.rect.topleft = (x,y)
        self.children.add(sprite)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.children.draw(screen)
