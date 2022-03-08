import monster
import pygame
import player
import video
import level
import sys

def init () :
    """
    @brief game initialization function

    @return player mode (0 = menu, 1 = explore and 2 = fight), screen, level
    """
    pygame.init ()

    # video
    screen = video.Video (2 / 3)

    # level genreration
    current_level = level.Level (generate_map (20, 20), player.Player (load_animation ("../img/test", 1), "P0"), [], [])

    return mode, screen, current_level

def generate_map (w, h) :
    return [[0 for i in range (w)] for j in range (h)]

def load_animation (path, n) :
    return [pygame.image.load (path + str (i)) for i in range (n)]

screen, current_level = init ()
mode = 0
played = False # if we have to resolve player action

# main loop ! CHANGE !
while True :

    # new level ?

    # events
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
    # draw

    pygame.display.flip ()