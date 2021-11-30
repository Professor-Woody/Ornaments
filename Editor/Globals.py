import pygame

#colours
BGCOLOR = (128,128,128)
LIGHTGREY = (192, 192, 192)
DARKGREY = (64, 64, 64)
TEXTCOLOR = (250, 250, 250)


# events
QUITEVENT = pygame.QUIT
LOADMP3EVENT = pygame.USEREVENT + 1
NEWPROGRAMEVENT = pygame.USEREVENT + 2
NEWORNAMENTEVENT = pygame.USEREVENT + 3
SAVEPROGRAMEVENT = pygame.USEREVENT + 4
FULLDRAWEVENT = pygame.USEREVENT + 5
ADDTIMEBAREVENT = pygame.USEREVENT + 6