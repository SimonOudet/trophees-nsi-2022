# -*- coding: utf-8 -*-

import monster
import random
import algo

class Stray (monster.Monster) :
    
    def __init__(self, anim, times, coord, hp, player) :
        super().__init__(anim, times, coord, hp)
        self.player = player
        self.agro = False
     
    def pulse (self, map:list, played:bool) :
        """
        A refresh function called each frame
        you can do what you want here

        input :
            - map : a double array wich represent a map of the level (see Level class)
            - played : if we have to resolve the player action
        """
        if played == True :
            if self.agro :
                self.coord = algo.a_star_path(self.map, self.coord, self.player)[0]
            else :
                posibilities = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                random.shuffle(posibilities)
                coordonnee = posibilities.pop()
                while not(algo.is_in_map(coordonnee, self.map)) and (self.map[coordonnee[0]][coordonnee[1]] != "_") :
                    coordonnee = posibilities.pop()
                self.coord = coordonnee