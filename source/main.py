# -*- coding: utf-8 -*-

import sequence
import pygame
import player
import stage
import video
import level
import boss
import sys

def init ()->list :
    """
    The game initialization function

    output :
        - the screen representation with a Video object
        - the level representation with a Level object
    """
    pygame.init ()

    # level genreration
    current_level = level.Level (generate_map (20, 20), player.Player (video.Video.load_animation ("test", 1), [1000], (5, 5), 20), [boss.Boss (video.Video.load_animation ("test", 1), [1000], (11, 5), 20, sequence.Sequence ([sequence.Action ("A", (0, 0))], [1000]))], [])

    # video
    screen = video.Video (2 / 3, len (current_level.get_map ()[0]))

    return screen, current_level

def generate_map (w:int, h:int)->list :
    """
    Genre a double array wich represent the map
    of the current level
    
    input : 
        - w : the width of the map
        - h : the height of the map
    output :
        - a double array wich represent the map
    """
    level = stage.stage_generator (23 * 2,
    [
        [
        ["M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", "#", "M"], 
        ["M", "#", "-", "B", "-", "#", "M"], 
        ["M", "#", "-", "-", "-", "#", "M"], 
        ["M", "#", "-", "-", "-", "#", "M"], 
        ["M", "#", "#", ".", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", ".", "#", "#", "M"], 
        ["M", "#", "-", "-", "-", "-", "-", "#", "M"], 
        ["M", "#", "B", "-", "-", "-", "-", "#", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M"], 
        ["M", " ", "#", "#", "#", "M"], 
        ["M", "#", "#", "-", "#", "M"], 
        ["M", "#", "-", "-", ".", "M"], 
        ["M", "#", "#", "B", "#", "M"], 
        ["M", " ", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", "#", "M"], 
        ["M", "#", "-", "B", "-", "#", "M"], 
        ["M", "#", "-", "-", "-", "#", "M"], 
        ["M", "#", "-", "-", "-", "#", "M"], 
        ["M", "#", "#", ".", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", ".", "#", "#", "M"], 
        ["M", "#", "-", "-", "-", "-", "-", "#", "M"], 
        ["M", "#", "B", "-", "-", "-", "-", "#", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M"], 
        ["M", " ", "#", "#", "#", "M"], 
        ["M", "#", "#", "-", "#", "M"], 
        ["M", "#", "-", "-", ".", "M"], 
        ["M", "#", "#", "B", "#", "M"], 
        ["M", " ", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M"]
        ]
    ])[0] # !TO CHANGE!
    #for i in level :
    #    print (i)
    return level

screen, current_level = init ()
key_cooldown = {97:False, 100:False, 119:False, 115:False}
played = False # if we have to resolve the player action

# main loop
while True :

    # new level ?

    # events
    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            sys.exit ()
        elif event.type == pygame.VIDEORESIZE :
            screen.change_screen_size (event.size)
        # keyboard
        if (pygame.key.get_pressed ()[97]) :        # left
            if (key_cooldown[97]) :
                key_cooldown[97] = False
            else :
                current_level.get_player ().move ((-1, 0), current_level.get_map ())
                played = True
                key_cooldown[97] = True
        elif (pygame.key.get_pressed ()[100]) :        # right
            if (key_cooldown[100]) :
                key_cooldown[100] = False
            else :
                current_level.get_player ().move ((1, 0), current_level.get_map ())
                played = True
                key_cooldown[100] = True
        elif (pygame.key.get_pressed ()[119]) :        # top
            if (key_cooldown[119]) :
                key_cooldown[119] = False
            else :
                current_level.get_player ().move ((0, -1), current_level.get_map ())
                played = True
                key_cooldown[119] = True
        elif (pygame.key.get_pressed ()[115]) :        # bottom
            if (key_cooldown[115]) :
                key_cooldown[115] = False
            else :
                current_level.get_player ().move ((0, 1), current_level.get_map ())
                played = True
                key_cooldown[115] = True

    # pulse
    for p in current_level.get_pulsable () :
        p.pulse (current_level.get_map (), played)
    played = False

    # animation
    screen.cancel ()
    for d in current_level.get_drawable (current_level.get_player ().get_pos ()) :
        surf, coor = d.draw ()
        screen.add (surf, coor)
    screen.refresh ()