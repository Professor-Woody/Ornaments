from Globals import *
from Element import *

class Text(Element):
    def __init__(self, text, position, size):
        Element.__init__(self)
        self.font = pygame.font.SysFont("arial", size)
        self.setText(text, position)

    def setText(self, text, position = None):
        if not position:
            position = self.rect.topleft

        self.image = self.font.render(text, 1, TEXTCOLOR)
        self.rect = self.image.get_rect()
        self.rect.move_ip(position)
        