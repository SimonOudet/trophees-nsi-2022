import pygame

class Video :
    def __init__ (self, coef):
        self.screen_size = pygame.display.get_desktop_sizes () [0]
        self.screen = pygame.display.set_mode ((self.screen_size [0] * coef, self.screen_size [1] * coef))
    
    def get_screen_size (self) :
        return self.screen_size

    def get_screen (self) :
        return self.screen

    def set_screen (self, screen) :
        self.screen = screen