# -*- coding: utf-8 -*-

import general as ge
import drawable
import monster
import player
import stray
import video
import algo

class Level :
    def __init__ (self, map:list, player:player.Player, bosses:list, vags:list, loots:list) :
        """
        Basic constructor of a Level object
        
        input :
            - map : a double array wich represent a map of the level ! TO COMPLETE !
            - player : the player of the level
            - bosses : an array with all the bosses of the level
            - vags : an array with all the vagabonds of the level
            - loots : an array with all the loots of the level
        """
        self.map = map
        self.load_map ()
        self.discover = {i.get_pos ():False for i in self.environment + self.door}
        self.player = player
        self.bosses = bosses
        self.vags = vags
        self.loots = loots
    
    def load_map (self) :
        """
        Load the drawables objects
        corresponding to the environment
        """
        self.environment = []
        self.door = []
        self.hiden_door = []
        self.hiden_environment = []
        for i in range (len (self.map)) :
            for j in range (len (self.map[i])) :
                if (self.map[i][j] == "-") or (self.map[i][j] == "_") or (self.map[i][j] == "P") or (self.map[i][j] == "A") : # ground
                    self.environment.append (drawable.Drawable ([video.Video.load_animation (ge.Val.GROUND_PATH + "_vis", ge.Val.GROUND_NB)], ge.Val.GROUND_TIMES, "G", (j, i)))
                    self.hiden_environment.append (drawable.Drawable ([video.Video.load_animation (ge.Val.GROUND_PATH + "_not_vis", ge.Val.GROUND_NB)], ge.Val.GROUND_TIMES, "G", (j, i)))
                elif (self.map[i][j] == "#") : # wall
                    self.environment.append (drawable.Drawable ([video.Video.load_animation (ge.Val.WALL_PATH + "_vis", ge.Val.WALL_NB)], ge.Val.WALL_TIMES, "G", (j, i)))
                    self.hiden_environment.append (drawable.Drawable ([video.Video.load_animation (ge.Val.WALL_PATH + "_not_vis", ge.Val.WALL_NB)], ge.Val.WALL_TIMES, "G", (j, i)))
                elif (self.map[i][j] == ".") : # door
                    self.door.append (drawable.Door ([video.Video.load_animation (ge.Val.DOOR_PATH + "_vis", ge.Val.DOOR_NB), video.Video.load_animation (ge.Val.LOCKED_DOOR_PATH + "_vis", ge.Val.LOCKED_DOOR_NB)], ge.Val.DOOR_TIMES, "G", (j, i)))
                    self.hiden_door.append (drawable.Door ([video.Video.load_animation (ge.Val.DOOR_PATH + "_not_vis", ge.Val.DOOR_NB), video.Video.load_animation (ge.Val.LOCKED_DOOR_PATH + "_not_vis", ge.Val.LOCKED_DOOR_NB)], ge.Val.DOOR_TIMES, "G", (j, i)))

    def update_map (self, x:int, y:int) :
        """
        A load map like function but optimized
        for a little change and only for ground
        changing in the boss context
        
        input :
            - x : the x coordinate
            - y : the y coordinate
        """
        i = algo.search_drawable (self.environment, (x, y))
        # an adding :
        if (i == -1) :
            self.discover[(x, y)] = True
            self.environment.insert (0, drawable.Drawable ([video.Video.load_animation (ge.Val.GROUND_PATH + "_vis", ge.Val.GROUND_NB)], ge.Val.GROUND_TIMES, "G", (x, y)))
            self.hiden_environment.insert (0, drawable.Drawable ([video.Video.load_animation (ge.Val.GROUND_PATH + "_not_vis", ge.Val.GROUND_NB)], ge.Val.GROUND_TIMES, "G", (x, y)))
        # a removing
        else :
            self.environment.pop (i)
            self.hiden_environment.pop (i)

    def get_map (self)->list :
        """
        Get the map of the level
        
        output :
            - the map of the level
        """
        return self.map

    def set_map (self, map:list) :
        """
        Create a map for this level
        
        input :
            - map : a double array wich represent a map of the new level ! TO COMPLETE !
        """
        self.map = map
        self.load_map ()
    
    def change_map (self, x:int, y:int, val:str) :
        """
        Change the map of the level
        
        input :
            - x : the x ccordinate
            - y : the y coordinate
            - val : the new value of this place
        """
        self.map [y][x] = val
        self.update_map (x, y) # ! CHANGE ! (only if an other entity than a boss use this function)
    
    def get_player (self)->player.Player :
        """
        Get the player of this level
        
        output :
            - the player
        """
        return self.player

    def get_monsters (self)->list :
        """
        Get all the monsters of this level
        
        output :
            - a list with all monsters 
        """
        return self.vags + self.bosses
    
    def get_bosses (self)->list :
        """
        Get all the bosses of this level
        
        output :
            - a list with all bosses 
        """
        return self.bosses

    def get_vagabonds (self)->list :
        """
        Get all the vagabonds of this level
        
        output :
            - a list with all vagabonds 
        """
        return self.vags
    
    def set_monsters (self, monsters:list, are_bosses=False) :
        """
        Modify all the monsters of the level
        
        input :
            - monsters : the new list of the level monsters
            - are_bosses : if the monsters are bosses
        """
        if (are_bosses) :
            self.bosses = monsters
        else :
            self.vags = monsters

    def change_monster (self, i:int, monster:monster.Monster, is_boss=False) :
        """
        Modify a monster of this level
        
        input :
            - i : the number of te monster
            - monster : the new monster
            - is_boss : if the monster is a boss
        """
        if (is_boss) :
            self.bosses [i] = monster
        else :
            self.vags [i] = monster

    def add_monsters (self, monsters:list, is_boss=False) :
        """
        Add some monsters to the level
        
        input :
            - monsters : a list of monsters objects
            - is_boss : if the monster is a boss
        """
        if (is_boss) :
            self.bosses += monsters
        else :
            self.vags += monsters

    def get_loots (self)->list :
        """
        Get all the loots of this level
        
        output :
            - a list with all loots 
        """
        return self.loots

    def set_loots (self, loots:list) :
        """
        Modify all the loots of the level
        
        input :
            - loots : the new list of the level loots
        """
        self.loots = loots

    def change_loot (self, i:int, loot:str) :
        """
        Modify a loot of this level
        
        input :
            - i : the number of the loot
            - loot : the new loot
        """
        self.loots [i] = loot

    def get_drawable (self, player_pos:tuple)->list :
        """
        Get all the drawable object of this level

        input :
            - player_pos : the player position
        output :
            - all the drawable object of this level
        """
        player_vision = []
        algo.manatan_vision (5, self.map, player_pos, player_vision, self.discover)
        return [i for i in self.hiden_environment if self.discover[i.get_pos ()]] + [door for door in self.hiden_door if self.discover[door.get_pos ()]] + [i for i in self.environment if i.get_pos () in player_vision] + [door for door in self.door if door.get_pos () in player_vision] + [self.player] + [boss for boss in self.bosses if boss.get_pos () in player_vision] + [vag for vag in self.vags if (vag.get_pos () in player_vision) and not vag.is_dead ()] # !CHANGE!

    def get_pulsable (self)->list :
        """
        Get all the pulsable object of this level

        output :
            - all the pulsable object of this level
        """
        return [self.player] + self.vags + self.bosses
    
    def lock_door (self, coord:tuple) :
        """
        Lock the door with the coord
        coordinates
        
        input :
            - coord : the coordinates of the door
        """
        i = algo.search_drawable (self.door, coord)
        print(i)
        self.door[i].lock ()
        self.hiden_door[i].lock ()