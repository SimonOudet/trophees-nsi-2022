# -*- coding: utf-8 -*-

class Val :

    PLAYER_PATH = "characters/hero"
    PLAYER_NB = 1
    PLAYER_TIMES = [1000]

    MONSTER_PATH = "characters/monster"
    MONSTER_NB = 1
    MONSTER_TIMES = [1000]

    GROUND_PATH = "terrain/ground"
    GROUND_NB = 1
    GROUND_TIMES = [1000]

    WALL_PATH = "terrain/wall"
    WALL_NB = 1
    WALL_TIMES = [1000]

    DOOR_PATH = "terrain/door"
    DOOR_NB = 1
    DOOR_TIMES = [1000]


    TIME_PLAY = 1
    MUSIC_TO_TIME = 1000 # to ms

class Room :
    def __init__ (self) :
        self.boss_position = ()
        self.door_position = ()
        self.orientation = None
    
    def set_boss_position (self, boss_position:tuple) :
        self.boss_position = boss_position
    
    def set_door_position (self, door_position:tuple) :
        self.door_position = door_position
    
    def set_orientation (self, orientation:str) :
        self.orientation = orientation
    
    def get_boss_position (self)->tuple :
        return self.boss_position
    
    def get_door_position (self)->tuple :
        return self.door_position
    
    def get_orientation (self)->str :
        return self.orientation