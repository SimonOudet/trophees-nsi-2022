# -*- coding: utf-8 -*-
import pygame

class Video :
    def __init__ (self, coef:int, map_width:int):
        """
        Basic constructor of a Video object
        which is an interface for the screen
        
        input :
            - coef : the fraction of the screen size used
        """
        self.map_width = map_width
        self.screen_size = pygame.display.get_desktop_sizes () [0]
        self.screen = pygame.display.set_mode ((self.screen_size [0] * coef, self.screen_size [1] * coef), pygame.RESIZABLE)
        self.zoom = int (self.screen.get_size ()[0] / self.map_width) # ! CHANGE !

    def change_screen_size (self, size:tuple) :
        """
        Change the size of the screen
        
        input :
            - size : the new screen size
        """
        pygame.transform.scale (self.screen, size)
        self.zoom = int (self.screen.get_size ()[0] / self.map_width) # ! CHANGE !

    def get_screen_size (self)->tuple :
        """
        Get the screen size
        
        output :
            - a tuple with the screen size
        """
        return self.screen_size

    def get_screen (self)->pygame.Surface :
        """
        Get the used screen
        
        output :
            - the used screen
        """
        return self.screen

    def set_screen (self, screen:pygame.Surface) :
        """
        Change the used screen

        input :
            - screen : the new screen
        """
        self.screen = screen

    def add (self, surf:pygame.Surface, coor:tuple) :
        """
        Draw a Surface into the screen

        input :
            - surf : the surface to draw
            - coor : the coordinates of the top left corner
        """
        self.screen.blit (pygame.transform.scale (surf, (self.zoom, self.zoom)), (coor[0] * self.zoom, coor[1] * self.zoom))

    def cancel (self) :
        """
        Reset the screen in black
        """
        self.screen.fill ("black")
    
    def refresh (self) :
        """
        Refresh the screen in order
        to make visible the changes
        """
        pygame.display.flip ()
    
    @staticmethod
    def load_animation (path:str, n:int)->list :
        """
        Return a list of Surface corresponding
        to a special animation
    
        input :
            - path : the path of the png file starting in the img directory and without the png extention \n
            - n : the number of frames \n
        output :
            - the list of Surface
        """
        return [pygame.image.load ("img/" + path + str (i) + ".png") for i in range (n)]