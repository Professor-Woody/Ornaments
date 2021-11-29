from Element import *
from Globals import *

class Ornament(Element):
    def __init__(self, ornamentId):
        Element.__init__(self)
        self.id = ornamentId
        font = pygame.font.SysFont("arial", 14)
        self.image = font.render("Ornament {}".format(ornamentId), 1, TEXTCOLOR)
        self.rect = self.image.get_rect()
        