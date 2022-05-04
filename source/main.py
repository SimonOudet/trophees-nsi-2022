# -*- coding: utf-8 -*-

import general as ge
import sequence
import pygame
import player
import music
import stray
import stage
import video
import level
import time
import boss
import sys

def init ()-> list :
    """
    The game initialization function

    output :
        - the screen representation with a Video object
        - the music representation with a Music object
        - the level representation with a Level object
    """
    pygame.init ()

    MOVE_SECOND = 10
    # level genreration
    map, rooms = generate_map (20, 20)
    # video
    screen = video.Video (2 / 3, rooms[0].get_boss_position ())
    # audio
    audio = music.Music (len (rooms) - 1,  [rooms[i].get_orientation () for i in range (1, len (rooms))]) # the first room is not a boss room
    current_level = level.Level (map, player.Player ([video.Video.load_animation (ge.Val.PLAYER_PATH, ge.Val.PLAYER_NB)], ge.Val.PLAYER_TIMES, rooms[0].get_boss_position (), 20, rooms, len (rooms), audio, screen, MOVE_SECOND), [], [], [])
    # add the bosses
    current_level.add_monsters ([boss.Boss ([video.Video.load_animation (ge.Val.BOSS_PATH + str (c - 1), ge.Val.BOSS_NB), video.Video.load_animation (ge.Val.BOSS_PATH + str (c - 1) + "_think", ge.Val.BOSS_NB)], ge.Val.BOSS_TIMES, rooms[c].get_boss_position (), rooms[c].get_activ_position (), 20, load_seq ("boss", c - 1, rooms[c].get_orientation ()), current_level, MOVE_SECOND) for c in range (1, len (rooms))], True) # !CHANGE!
    # add the vagabonds
    # current_level.add_monsters ([stray.Stray ([video.Video.load_animation (ge.Val.STRAY_PATH, ge.Val.STRAY_NB)], ge.Val.STRAY_TIMES, rooms[-1].get_boss_position (), 20, current_level.get_player (), MOVE_SECOND)])

    return screen, audio, current_level

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
    return stage.stage_generator (64 * 2,
    [
        [
        ["M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", "#", "M"], 
        ["M", "#", "-", "P", "-", "#", "M"], 
        ["M", "#", "-", "-", "-", "#", "M"], 
        ["M", "#", "-", "-", "-", "#", "M"], 
        ["M", "#", "#", ".", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M"]
        ],
        # saxo
        [
        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", "B", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", "A", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", "-", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", "#", "#", "#", ".", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"]
        ],
        #[
        #["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"], 
        #["M", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "M"], 
        #["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        #["M", "#", " ", " ", " ", " ", " ", " ", "B", " ", " ", "#", "M"], 
        #["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        #["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        #["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        #["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        #["M", "#", "5", "4", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        #["M", "#", "6", "3", "1", "A", " ", " ", " ", " ", " ", "#", "M"], 
        #["M", "#", " ", " ", "2", "-", " ", " ", " ", " ", " ", "#", "M"], 
        #["M", "#", "#", "#", "#", ".", "#", "#", "#", "#", "#", "#", "M"], 
        #["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"]
        #],
        # clar
        [
        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", "A", ".", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", "B", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"]
        ],
        # drums OK
        [
        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", ".", "A", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", " ", " ", " ", "B", "#", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"]
        ],
        # bass
        [
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"],
        ["M", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "#", "B", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", " ", " ", "#", "M"], 
        ["M", "#", " ", " ", " ", "A", " ", "#", "M"], 
        ["M", "#", "#", "#", "#", ".", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"]
        ],
        # trum OK
        [
        ["M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", "#", "M"], 
        ["M", "#", " ", " ", "B", "#", "M"], 
        ["M", "#", " ", " ", " ", "#", "M"], 
        ["M", ".", "A", " ", " ", "#", "M"], 
        ["M", "#", "#", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M"]
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
    time = -1
    type = "A"
    with open ('data/fights_sequences/' + name + str (i) + '.txt','r') as fichier :
        # for linux :
        for ligne in fichier :
            ligne = ligne.rstrip ('\n')
            if (len (ligne) == 0) :                 # ligne break = new actions
                seq.add_actions (actions, time)
                actions = []
                time = -1
            elif (time == -1) :                     # time
                time = int (ligne)
            elif (len (ligne) == 1) :               # type
                    type = ligne[0]
            else :                                  # coor
                x, y = tuple (map (int, ligne.split ()))
                if (orientation[0]) :               # we have to switch x and y
                    x, y = y, x
                actions.append (sequence.Action (type, (x * orientation[1][0], y * orientation[1][1])))
    return seq

screen, audio, current_level = init ()
played = False # if we have to resolve the player action

# main loop
while not current_level.get_player ().is_end () :

    # print (current_level.get_bosses ()[-1].get_current ()[0][0])

    # events
    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            sys.exit ()
        elif event.type == pygame.VIDEORESIZE :
                screen.change_screen_size (event.size)
        # keyboard
        if (pygame.key.get_pressed ()[pygame.K_a]) :
        # if (pygame.key.get_pressed ()[pygame.K_KP4]) :           # left
            dir = (-1, 0)
            played = True
        elif (pygame.key.get_pressed ()[pygame.K_d]) :
        # elif (pygame.key.get_pressed ()[pygame.K_KP6]) :         # right
            dir = (1, 0)
            played = True
        elif (pygame.key.get_pressed ()[pygame.K_w]) :
        # elif (pygame.key.get_pressed ()[pygame.K_KP8]) :         # top
            dir = (0, -1)
            played = True
        elif (pygame.key.get_pressed ()[pygame.K_s]) : 
        # elif (pygame.key.get_pressed ()[pygame.K_KP2]) :         # bottom
            dir = (0, 1)
            played = True
        elif (current_level.get_player ().is_fighting ()) :
            if (pygame.key.get_pressed ()[pygame.K_q]) :       # diagonal left top
                dir = (-1, -1)
                played = True
            elif (pygame.key.get_pressed ()[pygame.K_e]) :     # diagonal right top
                dir = (1, -1)
                played = True
            elif (pygame.key.get_pressed ()[pygame.K_z]) :     # diagonal left bottom
                dir = (-1, 1)
                played = True
            elif (pygame.key.get_pressed ()[pygame.K_x]) :     # diagonal right bottom
                dir = (1, 1)
                played = True
        
    if played : # the player has moved
        current_level.get_player ().move (dir, current_level.get_map (), current_level.get_bosses ())

    # pulse
    for p in current_level.get_pulsable () :            # note : the player always pulse before any monster
        p.pulse (current_level.get_map (), played)
    played = False

    # animation
    screen.cancel ()
    for d in current_level.get_drawable (current_level.get_player ().get_pos ()) :
        surf, coor = d.draw ()
        screen.add (surf, coor)
    screen.refresh ()
    time.sleep (0.01)

print ("GAME OVER")