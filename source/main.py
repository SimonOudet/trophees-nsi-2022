import monster
import pygame
import player
import video
import level
import sys

def init ()->list :
    """
    The game initialization function

    output : - the screen representation with a Video object
             - the level representation with a Level object
    """
    pygame.init ()

    # level genreration
    current_level = level.Level (generate_map (20, 20), player.Player (load_animation ("test", 1), [1000], (20, 20), 20), [], [])

    # video
    screen = video.Video (2 / 3)

    return screen, current_level

def generate_map (w:int, h:int)->list :
    """
    Genre a double array wich represent the map
    of the current level
    
    input : - w : the width of the map
            - h : the height of the map
    output : - a double array wich represent the map
    """
    return [[0 for i in range (w)] for j in range (h)]

def load_animation (path:str, n:int)->list :
    """
    Return a list of Surface corresponding
    to a special animation
    
    input : - path : the path of the png file starting in the img directory and without the png extention
            - n : the number of frames
    output : - the list of Surface
    """
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
    screen.refresh ()