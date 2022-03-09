import monster
import pygame
import player
import video
import level
import sys
import os

def init () :
    """
    @brief game initialization function

    @return player mode (0 = menu, 1 = explore), screen, level
    """
    pygame.init ()

    # level genreration
    current_level = level.Level (generate_map (20, 20), player.Player (load_animation ("test", 1), [1000],  "P0", (20, 20)), [], [])

    # video
    screen = video.Video (2 / 3)

    return screen, current_level

def generate_map (w, h) :
    return [[0 for i in range (w)] for j in range (h)]

def load_animation (path, n) :
    return [pygame.image.load ("img/" + path + str (i) + ".png") for i in range (n)]

screen, current_level = init ()
played = False # if we have to resolve player action

# main loop
while True :

    # new level ?

    # events
    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            sys.exit ()
    
    # pulse
    for p in current_level.get_pulsable () :
        p.pulse ()

    # animation
    screen.cancel ()
    for d in current_level.get_drawable () :
        surf, coor = d.draw ()
        screen.add (surf, coor)
    pygame.display.flip ()