import entity

class Player (entity.Entity) :
    def __init__ (self, anim:list, times:list, coord:tuple, hp:int):
        """
        Basic constructor of a Drawable object
        
        input : - anim : a list of all Surface used for the animation \n
                - times : a list of all times (in ms) of all frame of the animation \n
                - coord : the coordinates of the top left corner \n
                - hp : starting health points
        """
        super ().__init__ (anim, times, "P", coord, hp)