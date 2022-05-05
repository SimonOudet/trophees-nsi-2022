# -*- coding: utf-8 -*-

import monster
import random
import algo

class Stray (monster.Monster) :
    
    def __init__(self, anims, times, coord, hp, player, MOVE_SECOND:float) :
        super().__init__(anims, times, coord, hp, MOVE_SECOND)
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
                coo = algo.a_star_path(map, self.coord, self.player.get_pos ())[1]
                if (coo == self.player.get_pos ()) :
                    coo = self.coor
                    dammage = random.randint (5, 10)
                    self.player.set_health (self.player.get_health() - ((self.player.get_hp () * dammage) // 100))
                self.coor = coo
            else :
                posibilities = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                random.shuffle(posibilities)
                direction = posibilities.pop()
                coordonnee = (self.coord[0] + direction[0], self.coord[1] + direction[1])
                while not(algo.is_in_map(coordonnee, map)) or (map[coordonnee[1]][coordonnee[0]] == "#") :
                    direction = posibilities.pop()
                    coordonnee = (self.coord[0] + direction[0], self.coord[1] + direction[1])
                self.coord = coordonnee
                vision = []
                algo.manatan_vision (4, map, self.coord, vision, {})
                self.agro = self.player.get_pos () in vision