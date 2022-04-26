# -*- coding: utf-8 -*-

import entity

class Player (entity.Entity) :
    def __init__ (self, anim:list, times:list, coord:tuple, hp:int):
        """
        Basic constructor of a Drawable object
        
        input :
            - anim : a list of all Surface used for the animation
            - times : a list of all times (in ms) of all frame of the animation
            - coord : the coordinates of the top left corner
            - hp : starting health points
        """
        super ().__init__ (anim, times, "P", coord, hp)
        self.fighting = False
        self.destruct_path = ()
        self.boss = None
    
    def move (self, coor:tuple, map:list, bosses:list)->bool :
        """
        Move the entity
        
        input :
            - coor : the coordinates that will increase the currents coordinates
            - map : the level representation
            - bosses : a list of the bosses
        output :
            - if we have change our position
        """
        ret = super ().move (coor, map, self.destruct_path)
        if (map[self.coord[1]][self.coord[0]] == ".") and not self.fighting :
            print ("activation")
            self.fighting = True
            # find the door direction
            for dir in ((0, 1), (0, -1), (-1, 0), (1, 0)) :
                if (map[self.coord[1] + dir [1]][self.coord[0] + dir[0]] == "-") :
                    self.destruct_path = ((self.coord[0] - dir[0], self.coord[1] - dir [1]), ()) # strange, the second item is necessary
                    break
            # find the boss
            for boss in bosses :
                if (boss.get_activ () == self.coord) :
                    self.boss = boss
                    print ("find")
                    break
            self.boss.trigger ()
        return ret