import pygame


class Element(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect()


    def events(self, events):
        pass