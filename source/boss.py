# -*- coding: utf-8 -*-

import sequence
import entity
import pygame

class Boss (entity.Entity) :
    def __init__ (self, anim:list, times:list, coord:tuple, hp:int, sequence:sequence.Sequence):
        """
        Basic constructor of a boss object
        
        input :
            - anim : a list of all Surface used for the animation
            - times : a list of all times (in ms) of all frame of the animation
            - coord : the coordinates of the top left corner
            - hp : starting health points
            - sequence : the fight sequence
        """
        super ().__init__ (anim, times, "B", coord, hp)
        self.sequence = sequence
        self.music_clock = pygame.time.Clock ()
        self.music_time = 0
        self.current_action = sequence.get_action_time ()       # the action, the time
        self.is_active = False                                  # if the Boss is fighting
    
    def pulse (self, map:list, played:bool):
        """
        Used when the player is fighting against
        this boss and when it's her turn

        input :
            - map : a double array wich represent a map of the level (see Level class)
            - played : if we have to resolve the player action
        """
        if (self.is_active) :
            self.music_time = self.music_clock.tick ()
            if (self.music_time >= self.current_action [1]) :
                self.music_time = 0
                # do self.current_action [0]
                if (self.current_action [0] == "A") :               # an attack
                    self.attack (map, self.current_action [1])
                else :                                              # a move
                    self.go_to (self.current_action [1])
                self.current_action = self.sequence.get_action_time ()
    
    def attack (self, map:list, dest:list) :
        """
        Make an attack against all of the given coordinates

        input :
            - map : the level representation
            - dest : a list of coordinates
        """
        pass
