# -*- coding: utf-8 -*-

import monster
import algo

class Stray (monster.Monster) :
    
    def __init__(self, anim, times, coord, hp, player) :
        super().__init__(anim, times, coord, hp)
        self.player = player
        
    def stray_move (self) :
        self.coord = algo.a_star_path(self.map, self.coord, self.player)[0]
    