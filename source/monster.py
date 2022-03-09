import entity

class Monster (entity.Entity) :
    def __init__ (self, anim, times, ID, coord):
        super ().__init__ (anim, times, ID, coord)