import pygame

class RenderEvents(pygame.sprite.RenderUpdates):
    def __init__(self):
        pygame.sprite.RenderUpdates.__init__(self)

    def clear(self, screen, bg):
        for obj in self:
            try:
                obj.clear(screen, bg)
            except:
                screen.blit(bg.subsurface(obj.rect), obj.rect)

    def events(self, events):
        for obj in self:
            obj.events(events)

    def draw(self, screen):
        for obj in self:
            try:
                obj.draw(screen)
            except:
                screen.blit(obj.image, obj.rect)