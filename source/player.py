# -*- coding: utf-8 -*-

import general as ge
import entity
import pygame

class Player (entity.Entity) :
    def __init__ (self, anim:list, times:list, coord:tuple, hp:int, activs:list):
        """
        Basic constructor of a Drawable object
        
        input :
            - anim : a list of all Surface used for the animation
            - times : a list of all times (in ms) of all frame of the animation
            - coord : the coordinates of the top left corner
            - hp : starting health points
            - activs : a list of all the boss activation coord
        """
        super ().__init__ (anim, times, "P", coord, hp)
        self.fighting = False
        self.can_play = True        # if the player can play
        self.have_play = True       # if the player is in a playable duration
        self.destruct_path = ()
        self.boss = None
        self.time_wait = 0
        self.music_clock = pygame.time.Clock ()
        self.music_time = 0
        self.activs = activs
    
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
            ret = super ().move (coor, map, self.destruct_path)
        elif (self.can_play) :                                                                  # he's fighting but he can play
            ret = super ().move (coor, map, self.destruct_path)
            # self.can_play = False
        if (self.coord in self.activs) and not self.fighting :
            # print ("activation")
            self.fighting = True
            # find the door direction
            for dir in ((0, 1), (0, -1), (-1, 0), (1, 0)) :
                if (map[self.coord[1] + dir [1]][self.coord[0] + dir[0]] == ".") :
                    self.destruct_path = ((self.coord[0] - dir[0], self.coord[1] - dir [1]), ()) # strange, the second item is necessary
                    break
            # find the boss
            for boss in bosses :
                if (boss.get_activ () == self.coord) :
                    self.boss = boss
                    # print ("find")
                    break
            self.boss.trigger ()
            self.music_clock.tick ()
            print ("he's playing")
        elif self.fighting :
            self.fighting = not self.boss.is_dead ()
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