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
    map, bosses = generate_map (20, 20)
    current_level = level.Level (map, player.Player (video.Video.load_animation ("test", 1), [1000], (bosses[0][1], bosses[0][0]), 20), [], [])
    # add the bosses
    current_level.add_monsters ([boss.Boss (video.Video.load_animation ("test", 1), [1000], (c[1], c[0]), 20, sequence.Sequence ([sequence.Action ("A", (0, 0))], [1000])) for c in bosses[1:]]) # !CHANGE!

    # video
    screen = video.Video (2 / 3, (bosses[0][1], bosses[0][0]))

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
    return stage.stage_generator (23 * 2,
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
    ]) # !TO CHANGE!
    #for i in level :
    #    print (i)
    # return level, boss

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
                dir = (-1, 0)
                if (current_level.get_player ().move (dir, current_level.get_map ())) : # the player has moved
                    screen.move_origin (dir)
                played = True
                key_cooldown[97] = True
        elif (pygame.key.get_pressed ()[100]) :        # right
            if (key_cooldown[100]) :
                key_cooldown[100] = False
            else :
                dir = (1, 0)
                if (current_level.get_player ().move (dir, current_level.get_map ())) : # the player has moved
                    screen.move_origin (dir)
                played = True
                key_cooldown[100] = True
        elif (pygame.key.get_pressed ()[119]) :        # top
            if (key_cooldown[119]) :
                key_cooldown[119] = False
            else :
                dir = (0, -1)
                if (current_level.get_player ().move (dir, current_level.get_map ())) : # the player has moved
                    screen.move_origin (dir)
                played = True
                key_cooldown[119] = True
        elif (pygame.key.get_pressed ()[115]) :        # bottom
            if (key_cooldown[115]) :
                key_cooldown[115] = False
            else :
                dir = (0, 1)
                if (current_level.get_player ().move (dir, current_level.get_map ())) : # the player has moved
                    screen.move_origin (dir)
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