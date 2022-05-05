# -*- coding: utf-8 -*-

import general as ge
import sequence
import entity
import pygame
import level

class Boss (entity.Entity) :
    def __init__ (self, anims:list, times:list, coord:tuple, activ:tuple, hp:int, sequence:sequence.Sequence, level:level.Level, MOVE_SECOND:float):
        """
        Basic constructor of a boss object

        input :
            - anims : a list of list of all Surface used for the animation
            - times : a list of lis of all times (in ms) of all frames of the animation
            - coord : the coordinates of the top left corner
            - activ : the coordinates where the player activates the boss
            - hp : starting health points
            - sequence : the fight sequence
            - level : the level representation
            - MOVE_SECOND : the number of moves allowed for a second
        """
        super ().__init__ (anims, times, "B", coord, hp, MOVE_SECOND)
        print (self.ID)
        self.sequence = sequence
        self.music_clock = pygame.time.Clock ()
        self.music_time = 0
        self.current_action = sequence.get_actions_time ()      # the actions, the time
        self.is_active = False                                  # if the Boss is fighting
        self.activ = activ
        self.level = level
        self.dead = False
        self.think = False

    def pulse (self, map:list, played:bool):
        """
        Used when the player is fighting against
        this boss and when it's his turn

        input :
            - map : a double array wich represent a map of the level (see Level class)
            - played : if we have to resolve the player action
        """
        if (self.is_active) :
            self.music_time += self.music_clock.tick ()
            if (self.music_time >= self.current_action[1] * ge.Val.MUSIC_TO_TIME) :                         # the boss have to play
                print ("play")
                self.i_anim = 0                                                                             # not thinking
                self.music_time = 0
                # do the current actions
                for action in self.current_action[0] :
                    if (action.get_type () == "D") :                                                        # a remove
                        self.remove_floor (self.level, action.get_dest ()[0] + self.coord[0], action.get_dest ()[1] + self.coord[1])
                    else :                                                                                  # an adding
                        self.add_floor (self.level, action.get_dest ()[0] + self.coord[0], action.get_dest ()[1] + self.coord[1])
                if not (self.sequence.is_empty ()) :
                    self.current_action = self.sequence.get_actions_time ()
                else :
                    self.is_active = False
                    print ("DEAD")
                    self.dead = True
                self.music_time = 0
            elif (self.music_time >= ge.Val.TIME_PLAY * ge.Val.MUSIC_TO_TIME) :          # the boss is thinking
                print ("thinking")
                self.i_anim = 1                                                                             # thinking

    def remove_floor (self, level:level.Level, x:int, y:int) :
        """
        Removes the floor at the given coordinates

        input :
            - level : the level representation
            - x : the x coordinates
            - y : the y coordinates
        """
        level.change_map (x, y, " ")

    def add_floor (self, level:level.Level, x:int, y:int) :
        """
        Adds a floor at the given coordinates

        input :
            - level : the level representation
            - x : the x coordinates
            - y : the y coordinates
        """
        level.change_map (x, y, "-")

    def get_activ (self)->tuple :
        """
        Return the activation coordinates
        of the boss

        output :
            - the coordinates
        """
        return self.activ

    def trigger (self) :
        """
        Activation of the boss
        """
        self.is_active = True
        self.music_clock.tick ()
        print ("activation : ", self.ID)

    def get_current (self)-> tuple :
        """
        Returns the current action

        output :
            - the current action, a tuple (actions, time)
        """
        return self.current_action

    def is_dead (self)-> bool :
        """
        If the boss is dead

        output :
            - the boolean answer
        """
        return self.dead