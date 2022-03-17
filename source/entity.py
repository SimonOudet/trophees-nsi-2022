import drawable

class Entity (drawable.Drawable) :
    def __init__ (self, anim:list, times:list, ID:str, coord:tuple, hp:int):
        """
        Basic constructor of a entity object
        
        input : - anim : a list of all Surface used for the animation \n
                - times : a list of all times (in ms) of all frame of the animation \n
                - ID : unique identifier \n
                - coord : the coordinates of the top left corner \n
                - hp : starting health points
        """
        super ().__init__ (anim, times, ID, coord)
        self.hp = hp
    
    def get_health (self)->int :
        """
        Return the current amount of healt points
        
        output : - the current amount of healt points
        """
        return self.hp

    def set_health (self, val:int) :
        """
        Change the current amount of healt points
        
        input : - val : the new value
        """
        self.hp = val
    
    def add_health (self, val:int) :
        """
        Increase the current amount of healt points
        (use negative values for a decrease)
        
        input : - val : the value to add
        """
        self.hp += val

    def move (self, coor:tuple, map:list) :
        """
        Move the entity
        
        input : - coor : the coordinates that will increase the currents coordinates \n
                - map : the level representation
        """
        self.coord = (self.coord [0] + coor [0], self.coord [1] + coor [1])
        # !CHANGE MAP!
    
    def go_to (self, coor:tuple, map:list) :
        """
        Chnage the position of the entity
        
        input : - coor : the new coordinates \n
                - map : the level representation
        """
        self.coord = coor
        # !CHANGE MAP!