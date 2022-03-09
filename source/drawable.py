import imp
import pygame
import pulsable

class Drawable (pulsable.Pulsable) :
    def __init__ (self, anim, times, ID, coord) :
        self.clock = pygame.time.Clock ()
        self.anim = anim
        self.times = times
        self.coord = coord
        self.ID = ID
        self.time = 0
        self.i = 0
    
    def draw (self) :
        self.time += self.clock.tick ()
        if (self.time >= self.times [self.i]) :
            self.time = 0
            self.i += 1
            if (self.i == len (self.anim)) :
                self.i = 0
        return self.anim [self.i], self.coord