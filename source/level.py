
class Level :
    def __init__ (self, map, player, monsters, loots) :
        self.map = map
        self.player = player
        self.monsters = monsters
        self.loots = loots
    
    def get_map (self) :
        return self.map

    def set_map (self, map) :
        self.map = map
    
    def change_map (self, x, y, val) :
        self.map [y][x] = val
    
    def get_player (self) :
        return self.player

    def get_monsters (self) :
        return self.monsters

    def set_monsters (self, monsters) :
        self.monsters = monsters

    def change_monster (self, i, monster) :
        self.monsters [i] = monster

    def get_loots (self) :
        return self.loots

    def set_loots (self, loots) :
        self.loots = loots

    def change_loot (self, i, loot) :
        self.loots [i] = loot