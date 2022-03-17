import sequence
import pygame
import player
import video
import level
import boss
import sys

def init ()->list :
    """
    The game initialization function

    output : - the screen representation with a Video object \n
             - the level representation with a Level object
    """
    pygame.init ()

    # level genreration
    current_level = level.Level (generate_map (20, 20), player.Player (video.Video.load_animation ("test", 1), [1000], (20, 20), 20), [boss.Boss (video.Video.load_animation ("test", 1), [1000], (80, 80), 20, sequence.Sequence ([sequence.Action ("A", (0, 0))], [1000]))], [])

    # video
    screen = video.Video (2 / 3)

    return screen, current_level

def generate_map (w:int, h:int)->list :
    """
    Genre a double array wich represent the map
    of the current level
    
    input : - w : the width of the map \n
            - h : the height of the map \n
    output : - a double array wich represent the map
    """
    return [[" ", " ", " ", " ", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", "#", "-", "-", "-", "#", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", "#", "-", "-", "-", "#", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", "#", "-", "-", "-", "#", " ", " ", "#", "#", "#", "#", "#", "#", "#"],
            [" ", " ", " ", "#" ,"#", "#", "-", "#", "#", "#", "#", "#", "-", "#", "-", "-", "-", "#"],
            [" ", " ", " ", "#", "-", "-", "-", "-", "-", "#", "#", "-", "-", "-", "-", "-", "-", "#"],
            ["#", "#", "#", "#", "-", "#", "#", "#", "-", "-", "#", "#", "-", "#", "-", "-", "#", "#"],
            ["#", "-", "-", "-", "-", "-", "#", "#", "#", "-", "#", "#", "#", "#", "-", "#", "#", " "],
            ["#", "-", "-", "-", "-", "-", "#", " ", "#", "-", "-", "-", "-", "-", "-", "#", " ", " "],
            ["#", "#", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", " "]]

screen, current_level = init ()
played = False # if we have to resolve player action

# main loop
while True :

    # new level ?

    # events
    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            sys.exit ()
        elif event.type == pygame.VIDEORESIZE :
            screen.change_screen_size (event.size)
    
    # pulse
    for p in current_level.get_pulsable () :
        p.pulse (current_level.get_map ())

    # animation
    screen.cancel ()
    for d in current_level.get_drawable () :
        surf, coor = d.draw ()
        screen.add (surf, coor)
    screen.refresh ()