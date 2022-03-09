import pygame

class Video :
    def __init__ (self, coef:int):
        """
        Basic constructor of a Video object
        which is an interface for the screen
        
        input : - coef : the fraction of the screen size used
        """
        self.screen_size = pygame.display.get_desktop_sizes () [0]
        self.screen = pygame.display.set_mode ((self.screen_size [0] * coef, self.screen_size [1] * coef))
    
    def get_screen_size (self)->tuple :
        """
        Get the screen size
        
        output : - a tuple with the screen size
        """
        return self.screen_size

    def get_screen (self)->pygame.Surface :
        """
        Get the used screen
        
        output : the used screen
        """
        return self.screen

    def set_screen (self, screen:pygame.Surface) :
        """
        Change the used screen

        input : - screen : the new screen
        """
        self.screen = screen

    def add (self, surf:pygame.Surface, coor:tuple) :
        """
        Draw a Surface into the screen

        input : - surf : the surface to draw
                - coor : the coordinates of the top left corner
        """
        self.screen.blit (surf, coor)

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