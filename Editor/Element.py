import pygame

from RenderEvents import RenderEvents


class Element(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()

    def events(self, events):
        pass
    
    def move(self, offset):
        self.rect.move_ip(offset)
        
    def amove(self, position):
        self.rect.topleft = position
    
    
class ParentElement(Element):
    def __init__(self):
        Element.__init__(self)
        self.children = RenderEvents()
        
    def clear(self, screen, bg):
        self.children.clear(screen, bg)
        screen.blit(bg.subsurface(self.rect), self.rect)
        
    def update(self):
        self.children.update()
        
    def events(self, events):
        self.children.events(events)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.children.draw(screen)
        
        
    def add(self, sprite):
        self.children.add(sprite)
        
    def remove(self, sprite):
        self.children.remove(sprite)
    
    def move(self, offset):
        for child in self.children:
            child.move(offset)
        Element.move(self, offset)
    
    # absolute move   
    def amove(self, position):
        delta = (position[0] - self.rect.x, position[1] - self.rect.y)
        Element.amove(self, position)
        
        for child in self.children:
            child.move(delta)
        