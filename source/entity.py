import drawable

class Entity (drawable.Drawable) :
    def __init__ (self, anim, times, ID, coord):
        super ().__init__ (anim, times, ID, coord)
        self.state = 0
        self.hp = 20
    
    def get_health (self) :
        return self.hp

    def set_health (self, val) :
        self.hp = val
    
    def add_health (self, val) :
        self.hp += val