import entity

class Monster (entity.Entity) :
    def __init__ (self, anim:list, times:list, coord:tuple, hp:int):
        """
        Basic constructor of a Monster object
        
        input : - anim : a list of all Surface used for the animation
                - times : a list of all times (in ms) of all frame of the animation
                - ID : unique identifier (M + number)
                - coord : the coordinates of the top left corner
                - hp : starting health points
        """
        super ().__init__ (anim, times, "M", coord, hp)