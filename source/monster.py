# -*- coding: utf-8 -*-

import entity

class Monster (entity.Entity) :
    def __init__ (self, anims:list, times:list, coord:tuple, hp:int, MOVE_SECOND:float):
        """
        Basic constructor of a Monster object
        
        input :
            - anim : a list of list of all Surface used for the animation
            - times : a list of list of all times (in ms) of all frame of the animation
            - coord : the coordinates of the top left corner
            - hp : starting health points
            - MOVE_SECOND : the number of moving allowed for a second
        """
        super ().__init__ (anims, times, "M", coord, hp, MOVE_SECOND)