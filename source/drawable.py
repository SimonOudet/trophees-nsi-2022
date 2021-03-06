# -*- coding: utf-8 -*-

import pygame
import pulsable

class Drawable (pulsable.Pulsable) :

    counter = 0 # static attribute wich count the number of Drawable pbject created
    def __init__ (self, anims:list, times:list, ID:str, coord:tuple) :
        """
        Basic constructor of a Drawable object
        
        input :
            - anim : a list of list of all Surface used for the animation
            - times : a list of list of all times (in ms) of all frame of the animation
            - ID : unique identifier type (P, M...)
            - coord : the coordinates of the top left corner
        """
        # assert len (anim) == len (times), "the number of frames does not match with the nuber of times"
        self.anims = anims
        self.i_anim = 0 # the animation index
        self.coord = coord
        self.clock = pygame.time.Clock ()
        self.times = times
        self.time = 0
        self.i = 0 # current frame
        self.ID = ID + str (Drawable.counter)
        Drawable.counter += 1
    
    def get_pos (self)->tuple :
        return self.coord

    def draw (self)-> list :
        """
        Function to call each frame

        output :
            - the surface of the current frame
            - the coordinates of the top left corner
        """
        self.time += self.clock.tick ()
        if (self.time >= self.times [self.i_anim][self.i]) : # change frame
            self.time = 0
            self.i += 1
            if (self.i == len (self.anims[self.i_anim])) :
                self.i = 0
        return self.anims [self.i_anim][self.i], self.coord
    
    def __str__ (self) -> str:
        return self.ID

class Door (Drawable) :
    def __init__ (self, anims:list, times:list, ID:str, coord:tuple) :
        """
        Basic constructor of a Drawable object
        
        input :
            - anim : a list of list of all Surface used for the animation
            - times : a list of list of all times (in ms) of all frame of the animation
            - ID : unique identifier type (P, M...)
            - coord : the coordinates of the top left corner
        """
        super ().__init__ (anims, times, ID, coord)
    
    def lock (self) :
        """
        Switch from a unlocked texture
        to a locked
        """
        self.i_anim = 1