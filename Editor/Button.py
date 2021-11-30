import pygame
from Element import *
from Globals import *

class Button(Element):
    def __init__(self, text, position, size, event):
        Element.__init__(self)
        font = pygame.font.SysFont("arial", size)
        self.baseImage = font.render(text, 1, TEXTCOLOR)
        self.hoverOverImage = font.render(text, 1, TEXTCOLOR, BGCOLOR)

        self.image = self.baseImage
        self.rect = self.image.get_rect()
        self.rect.move_ip(position)        
        self.event = event

        self.hovering = False

    def events(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(pos):
                    if not self.hovering:
                        self.hovering = True
                        self.image = self.hoverOverImage
                else:
                    if self.hovering:
                        self.hovering = False
                        self.image = self.baseImage
                    
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(pos):
                    print ("button posting event {}".format(self.event.type))
                    pygame.event.post(self.event)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
