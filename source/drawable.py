import imp
import pygame
import pulsable

class Drawable (pulsable.Pulsable) :
    def __init__ (self, anim, ID) :
        self.clock = pygame.time.get_ticks ()
        self.anim = anim
        self.ID = ID
    
    def draw (self) :
        pass