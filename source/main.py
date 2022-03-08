import pygame
import sys

def init () :
    pass

pygame.init ()
size = pygame.display.get_desktop_sizes () [0]
screen = pygame.display.set_mode ((size [0] * 2 / 3, size [1] * 2 / 3))
mode = 0

init ()

# main loop
while True :

    # new level ?

    # event
    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            sys.exit ()
    
    if mode == 0 : # menu
        pass
    elif mode == 1 : # explore
        pass
    elif mode == 2 : # fight
        pass
    
    screen.fill ("black")

    # anim

    pygame.display.flip ()