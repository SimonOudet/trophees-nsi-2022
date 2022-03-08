import drawable

class Entity (drawable.Drawable) :
    def __init__ (self, anim, ID):
        super ().__init__ (anim, ID)
        self.state = 0
        self.HP = 20
    
    