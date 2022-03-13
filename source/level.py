import monster
import player

class Level :
    def __init__ (self, map:list, player:player.Player, monsters:list, loots:list) :
        """
        Basic constructor of a Level object
        
        input : - map : a double array wich represent a map of the level ! TO COMPLETE !
                - player : the player of the level
                - monsters : an array with all the monsters of the level
                - loots : an array with all the loots of the level
        """
        self.map = map
        self.player = player
        self.monsters = monsters
        self.loots = loots
    
    def get_map (self)->list :
        """
        Get the map of the level
        
        output : - the map of the level
        """
        return self.map

    def set_map (self, map:list) :
        """
        Create a map for this level
        
        input : - map : a double array wich represent a map of the new level ! TO COMPLETE !
        """
        self.map = map
    
    def change_map (self, x:int, y:int, val:str) :
        """
        Change the map of the level
        
        input : - x : the x ccordinate
                - y : the y coordinate
                - val : the new value of this place
        """
        self.map [y][x] = val
    
    def get_player (self)->player.Player :
        """
        Get the player of this level
        
        output : - the player
        """
        return self.player

    def get_monsters (self)->list :
        """
        Get all the monsters of this level
        
        output : - a list with all monsters 
        """
        return self.monsters

    def set_monsters (self, monsters:list) :
        """
        Modify all the monsters of the level
        
        input : - monsters : the new list of the level monsters
        """
        self.monsters = monsters

    def change_monster (self, i:int, monster:monster.Monster) :
        """
        Modify a monster of this level
        
        input : - i : the number of te monster
                - monster : the new monster
        """
        self.monsters [i] = monster

    def get_loots (self)->list :
        """
        Get all the loots of this level
        
        output : - a list with all loots 
        """
        return self.loots

    def set_loots (self, loots:list) :
        """
        Modify all the loots of the level
        
        input : - loots : the new list of the level loots
        """
        self.loots = loots

    def change_loot (self, i:int, loot:str) :
        """
        Modify a loot of this level
        
        input : - i : the number of the loot
                - loot : the new loot
        """
        self.loots [i] = loot

    def get_drawable (self)->list :
        """
        Get all the drawable object of this level

        output : all the drawable object of this level
        """
        return [self.player] + self.monsters

    def get_pulsable (self)->list :
        """
        Get all the pulsable object of this level

        output : all the pulsable object of this level
        """
        return [self.player] + self.monsters