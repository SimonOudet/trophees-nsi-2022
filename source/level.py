# -*- coding: utf-8 -*-

import basic_math as ma
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
        self.discover = {i.get_pos ():False for i in self.environment}
        self.player = player
        self.bosses = bosses
        self.vags = vags
        self.loots = loots
    
    def load_map (self) :
        """
        Loads the drawables objects
        corresponding to the environment
        """
        self.environment = []
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
                    self.environment.append (drawable.Drawable ([video.Video.load_animation (ge.Val.DOOR_PATH + "_vis", ge.Val.DOOR_NB)], ge.Val.DOOR_TIMES, "G", (j, i)))
                    self.hiden_environment.append (drawable.Drawable ([video.Video.load_animation (ge.Val.DOOR_PATH + "_not_vis", ge.Val.DOOR_NB)], ge.Val.DOOR_TIMES, "G", (j, i)))

    def update_map (self, x:int, y:int) :
        """
        A load map like function but optimized
        for a little change and only for ground
        changing in the bossfight context
        
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
        Returns the map of the level
        
        output :
            - the map of the level
        """
        return self.map

    def set_map (self, map:list) :
        """
        Creates a map for this level
        
        input :
            - map : a double array wich represents a map of the new level
        """
        self.map = map
        self.load_map ()
    
    def change_map (self, x:int, y:int, val:str) :
        """
        Changes the map of the level
        
        input :
            - x : the x coordinate
            - y : the y coordinate
            - val : the new value at the coordinates
        """
        self.map [y][x] = val
        self.update_map (x, y) # ! CHANGE ! (only if an other entity than a boss uses this function)
    
    def get_player (self)->player.Player :
        """
        Returns the player of this level
        
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
        Returns all the bosses of this level
        
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
        Modifies all the monsters of the level
        
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
        Modifies a monster of this level
        
        input :
            - i : the number of the monster
            - monster : the new monster
            - is_boss : if the monster is a boss
        """
        if (is_boss) :
            self.bosses [i] = monster
        else :
            self.vags [i] = monster

    def add_monsters (self, monsters:list, is_boss=False) :
        """
        Adds some monsters to the level
        
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
        Returns all the loot of this level
        
        output :
            - a list with all loots 
        """
        return self.loots

    def set_loots (self, loots:list) :
        """
        Modifies the loot of the level
        
        input :
            - loots : the new list of the level loots
        """
        self.loots = loots

    def change_loot (self, i:int, loot:str) :
        """
        Modifies a loot of this level
        
        input :
            - i : the number of the loot
            - loot : the new loot
        """
        self.loots [i] = loot

    def get_drawable (self, player_pos:tuple)->list :
        """
        Returns all the drawable objects of this level

        input :
            - player_pos : the player position
        output :
            - all the drawable objects of this level
        """
        player_vision = []
        algo.manatan_vision (5, self.map, player_pos, player_vision, self.discover)
        return [i for i in self.hiden_environment if self.discover[i.get_pos ()]] + [i for i in self.environment if i.get_pos () in player_vision] + [self.player] + [boss for boss in self.bosses if boss.get_pos () in player_vision] + [vag for vag in self.vags if vag.get_pos () in player_vision] # !CHANGE!

    def get_pulsable (self)->list :
        """
        Get all the pulsable objects of this level

        output :
            - all the pulsable objects of this level
        """
        return [self.player] + self.vags + self.bosses