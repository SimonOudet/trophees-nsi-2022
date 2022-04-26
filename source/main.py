# -*- coding: utf-8 -*-

import general as ge
import sequence
import pygame
import player
import stray
import stage
import video
import level
import time
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
    map, rooms = generate_map (20, 20)
    current_level = level.Level (map, player.Player (video.Video.load_animation (ge.Val.PLAYER_PATH, ge.Val.PLAYER_NB), ge.Val.PLAYER_TIMES, rooms[0].get_boss_position (), 20), [], [], [])
    # add the bosses
    current_level.add_monsters ([boss.Boss (video.Video.load_animation (ge.Val.MONSTER_PATH, ge.Val.MONSTER_NB), ge.Val.MONSTER_TIMES, rooms[c].get_boss_position (), rooms[c].get_door_position (), 20, load_seq ("boss", c, rooms[c].get_orientation ()), current_level) for c in range (len (rooms))], True) # !CHANGE!
    # add the vagabonds
    current_level.add_monsters ([stray.Stray (video.Video.load_animation (ge.Val.MONSTER_PATH, ge.Val.MONSTER_NB), ge.Val.MONSTER_TIMES, rooms[1].get_boss_position (), 20, current_level.get_player ())])
    # video
    screen = video.Video (2 / 3, rooms[0].get_boss_position ())

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
    return stage.stage_generator (60 * 2,
    [
        [
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", "B", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", ".", "-", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"]
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

def load_seq (name:str, i:int, orientation:tuple)->sequence.Sequence :
    """
    Load, from a txt file, a sequence
    
    input :
        - name : the name of the file (boss for a boss...)
        - i : the index
        - orientation : the orientation (a tuple with : (if we have to switch x and y, a tupple for the coordinates)
    output :
        - the sequence
    """
    seq = sequence.Sequence ()
    actions = []
    time = 0
    type = "A"
    with open ('data/' + name + str (i) + '.txt','r') as fichier :
        # for linux :
        for ligne in fichier :
            ligne = ligne.rstrip ('\n')
            if (len (ligne) == 0) :                 # ligne break = new actions
                seq.add_actions (actions, time)
                actions = []
                time = 0
            elif (time == 0) :                      # time
                time = int (ligne)
            elif (len (ligne) == 1) :               # type
                    type = ligne[0]
            else :                                  # coor
                x, y = tuple (map (int, ligne.split ()))
                if (orientation[0]) :               # we have to switch x and y
                    x, y = y, x
                actions.append (sequence.Action (type, (x * orientation[1][0], y * orientation[1][1])))
    return seq

screen, current_level = init ()
key_cooldown = {97:False, 100:False, 119:False, 115:False}
played = False # if we have to resolve the player action

# main loop
while True :

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
                if (current_level.get_player ().move (dir, current_level.get_map (), current_level.get_bosses ())) : # the player has moved
                    screen.move_origin (dir)
                played = True
                key_cooldown[97] = True
        elif (pygame.key.get_pressed ()[100]) :        # right
            if (key_cooldown[100]) :
                key_cooldown[100] = False
            else :
                dir = (1, 0)
                if (current_level.get_player ().move (dir, current_level.get_map (), current_level.get_bosses ())) : # the player has moved
                    screen.move_origin (dir)
                played = True
                key_cooldown[100] = True
        elif (pygame.key.get_pressed ()[119]) :        # top
            if (key_cooldown[119]) :
                key_cooldown[119] = False
            else :
                dir = (0, -1)
                if (current_level.get_player ().move (dir, current_level.get_map (), current_level.get_bosses ())) : # the player has moved
                    screen.move_origin (dir)
                played = True
                key_cooldown[119] = True
        elif (pygame.key.get_pressed ()[115]) :        # bottom
            if (key_cooldown[115]) :
                key_cooldown[115] = False
            else :
                dir = (0, 1)
                if (current_level.get_player ().move (dir, current_level.get_map (), current_level.get_bosses ())) : # the player has moved
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
    time.sleep (0.01)