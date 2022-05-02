# -*- coding: utf-8 -*-

import general as ge
import entity
import pygame
import music

class Player (entity.Entity) :
    def __init__ (self, anim:list, times:list, coord:tuple, hp:int, rooms:list, nb_boss:int, music:music.Music, MOVE_SECOND:float):
        """
        Basic constructor of a Drawable object
        
        input :
            - anim : a list of all Surface used for the animation
            - times : a list of all times (in ms) of all frame of the animation
            - coord : the coordinates of the top left corner
            - hp : starting health points
            - rooms : a list of all the rooms representation of the level
            - nb_boss : the number of boss of the level
            - music : the music manager
            - MOVE_SECOND : the number of moving allowed for a second
        """
        super ().__init__ (anim, times, "P", coord, hp, MOVE_SECOND)
        self.fighting = False
        self.can_play = True        # if the player can play
        self.have_play = True       # if the player is in a playable duration
        self.forbiden_paths = []
        self.boss = None
        self.time_wait = 0
        self.music_clock = pygame.time.Clock ()
        self.music_time = 0
        self.rooms = rooms
        self.ib = None              # the boss index
        self.nb_living_boss = nb_boss
        self.music = music
    
    def move (self, coor:tuple, map:list, bosses:list)->bool :
        """
        Move the entity
        
        input :
            - coor : the coordinates that will increase the currents coordinates
            - map : the level representation
            - bosses : a list of the bosses
        output :
            - if we have change our position
        """
        ret = False
        if not self.fighting :                                                                  # normal, he's not fighting
            ret = super ().move (coor, map, self.forbiden_paths)
        elif (self.can_play) :                                                                  # he's fighting but he can play
            ret = super ().move (coor, map, self.forbiden_paths)
            self.music.move (coor)
            self.can_play = False
        for i in range (1, len (self.rooms)) :                                                  # starting with 1, 0 is the player starting room
            if (self.coord == self.rooms[i].get_activ_position ()) :                            # we are in a boss activation position
                self.ib = i - 1                                                                 # -1 beacause of the first room, the player starting room
                self.forbiden_paths.append (self.rooms[i].get_door_position ())
                break
        if (self.ib != None) and not self.fighting :                                            # we juste activate a boss
            self.fighting = True
            self.boss = bosses[self.ib]
            self.boss.trigger ()
            self.music.start_fight (self.ib)
            self.music_clock.tick ()
            print ("he's playing")
        return ret
    
    def pulse (self, map:list, played:bool) :
        """
        A refresh function called each frame
        you can do what you want here

        input :
            - map : a double array wich represent a map of the level (see Level class)
            - played : if we have to resolve the player action
        """
        # print (self.can_play and self.have_play)
        if self.fighting :
            self.music_time += self.music_clock.tick ()
            if self.have_play and (self.music_time >= ge.Val.TIME_PLAY * ge.Val.MUSIC_TO_TIME) :        # he have to play AND it's the end
                self.have_play = False
                self.can_play = False
                self.music_time = 0
                self.time_wait = self.boss.get_current ()[1]
                print ("he's waiting")
            elif not self.have_play and (self.music_time >= self.time_wait * ge.Val.MUSIC_TO_TIME) :    # he's waiting AND it's the end
                self.have_play = True
                self.can_play = True
                self.music_time = 0
                print ("he's playing")
            elif self.boss.is_dead () :                                                                 # ending of the fight
                self.fighting = False
                self.music.stop_fight ()
                self.go_to ((self.rooms[self.ib + 1].get_door_position ()), map)                        # +1 beacause of the first room, the player starting room
                self.forbiden_paths.append (self.rooms[self.ib + 1].get_activ_position ())
                print ("TP")
                self.ib = None
                self.nb_living_boss -= 1
    
    def is_fighting (self)->bool :
        """
        If the player is fighting against
        a boss

        output :
            - the boolean value
        """
        return self.fighting
    
    def is_end (self)-> bool :
        """
        If the player has
        beaten all of the boss
        of the level

        output :
            - the boolean value
        """
        return self.nb_living_boss == 0