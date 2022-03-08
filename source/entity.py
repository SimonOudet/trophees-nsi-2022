import drawable

class Entity (drawable.Drawable) :
    def __init__ (self, anim, ID):
        super ().__init__ (anim, ID)
        self.state = 0
        self.hp = 20
    
    def get_health (self) :
        return self.hp

    def set_health (self, val) :
        self.hp = val
    
    def add_health (self, val) :
        self.hp += val