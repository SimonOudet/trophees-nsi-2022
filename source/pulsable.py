# -*- coding: utf-8 -*-

class Pulsable :
    def pulse (self, map:list, played:bool, player_pos:tuple) :
        """
        A refresh function called each frame
        you can do what you want here

        input :
            - map : a double array wich represent a map of the level (see Level class)
            - played : if we have to resolve the player action
            - player_pos : the player position
        """