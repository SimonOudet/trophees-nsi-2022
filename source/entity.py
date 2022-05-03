# -*- coding: utf-8 -*-

import drawable
import pygame

class Entity (drawable.Drawable) :
    def __init__ (self, anims:list, times:list, ID:str, coord:tuple, hp:int, MOVE_SECOND:float):
        """
        Basic constructor of a entity object
        
        input :
            - anims : a list of list of all Surface used for the animation
            - times : a list of list of all times (in ms) of all frame of the animation
            - ID : unique identifier
            - coord : the coordinates of the top left corner
            - hp : starting health points
            - MOVE_SECOND : the number of moving allowed for a second
        """
        super ().__init__ (anims, times, ID, coord)
        self.hp = hp
        self.moving_clock = pygame.time.Clock ()
        self.moving_time = 0
        self.MOVE_SECOND = MOVE_SECOND
    
    def get_health (self)->int :
        """
        Return the current amount of healt points
        
        output :
            - the current amount of healt points
        """
        return self.hp

    def set_health (self, val:int) :
        """
        Change the current amount of healt points
        
        input :
            - val : the new value
        """
        self.hp = val
    
    def add_health (self, val:int) :
        """
        Increase the current amount of healt points
        (use negative values for a decrease)
        
        input :
            - val : the value to add
        """
        self.hp += val

    def move (self, coor:tuple, map:list, forbiden=[])->bool :
        """
        Move the entity
        
        input :
            - coor : the coordinates that will increase the currents coordinates
            - map : the level representation
            - forbiden : a list of tuple with positions forbiden
        output :
            - if we have change our position
        """
        self.moving_time += self.moving_clock.tick ()
        if (self.moving_time >= 1000 / self.MOVE_SECOND) :
            self.moving_time = 0
            x = self.coord [0] + coor [0]
            y = self.coord [1] + coor [1]
            size = (len (map[0]), len (map))
            if (x < size[0]) and (x >= 0) and (y < size[1]) and (y >= 0) and (map[y][x] != "#") and ((x, y) not in forbiden) :
                self.coord = (self.coord [0] + coor [0], self.coord [1] + coor [1])
                return True
        return False
    
    def go_to (self, coor:tuple, map:list) :
        """
        Chnage the position of the entity
        
        input :
            - coor : the new coordinates
            - map : the level representation
        """
        size = (len (map[0]), len (map))
        if (coor[0] < size[0]) and (coor[0] >= 0) and (coor[1] < size[1]) and (coor[1] >= 0) and (map[coor[1]][coor[0]] != "#") :
            self.coord = coor
            return True
        return False