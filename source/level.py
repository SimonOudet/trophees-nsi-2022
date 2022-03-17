import general as ge
import drawable
import monster
import player
import video

class Level :
    def __init__ (self, map:list, player:player.Player, monsters:list, loots:list) :
        """
        Basic constructor of a Level object
        
        input : - map : a double array wich represent a map of the level ! TO COMPLETE ! \n
                - player : the player of the level \n
                - monsters : an array with all the monsters of the level \n
                - loots : an array with all the loots of the level
        """
        self.map = map
        self.load_map ()
        self.player = player
        self.monsters = monsters
        self.loots = loots
    
    def load_map (self)->list :
        self.environment = []
        for i in range (len (self.map)) :
            for j in range (len (self.map[i])) :
                if (self.map[i][j] == "-") : # ground
                    self.environment.append (drawable.Drawable (video.Video.load_animation (ge.Val.GROUND_PATH, ge.Val.GROUND_NB), ge.Val.GROUND_TIMES, "G", (j, i)))
                elif (self.map[i][j] == "#") : # wall
                    self.environment.append (drawable.Drawable (video.Video.load_animation (ge.Val.WALL_PATH, ge.Val.WALL_NB), ge.Val.WALL_TIMES, "G", (j, i)))

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
        self.load_map ()
    
    def change_map (self, x:int, y:int, val:str) :
        """
        Change the map of the level
        
        input : - x : the x ccordinate \n
                - y : the y coordinate \n
                - val : the new value of this place
        """
        self.map [y][x] = val
        self.load_map () # ! CHANGE !
    
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
        
        input : - i : the number of te monster \n
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
        
        input : - i : the number of the loot \n
                - loot : the new loot
        """
        self.loots [i] = loot

    def get_drawable (self)->list :
        """
        Get all the drawable object of this level

        output : all the drawable object of this level
        """
        return [self.player] + self.monsters + self.environment

    def get_pulsable (self)->list :
        """
        Get all the pulsable object of this level

        output : all the pulsable object of this level
        """
        return [self.player] + self.monsters