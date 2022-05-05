# -*- coding: utf-8 -*-

import random
import general as ge
import entity
import pygame
import music
import video

class Player (entity.Entity) :
    def __init__ (self, anims:list, times:list, coord:tuple, hp:int, damage:int, rooms:list, nb_boss:int, music:music.Music, video:video.Video, MOVE_SECOND:float, starting_vision=5):
        """
        Basic constructor of a Drawable object

        input :
            - anims : a list of list of all Surface used for the animation
            - times : a list of list of all times (in ms) of all frame of the animation
            - coord : the coordinates of the top left corner
            - hp : starting health points
            - damage : the amout of damage the player deals every attack
            - rooms : a list of all the rooms representation of the level
            - nb_boss : the number of boss of the level
            - music : the music manager
            - video : the video manager
            - MOVE_SECOND : the number of moving allowed for a second
            - starting_vision : the starting vision range of the player
        """
        super ().__init__ (anims, times, "P", coord, hp, MOVE_SECOND)
        self.fighting = False
        self.can_play = True        # if the player can play
        self.have_play = True       # if the player is in a playable duration
        self.forbiden_paths = []
        self.boss = None
        self.damage = damage
        self.time_wait = 0
        self.music_clock = pygame.time.Clock ()
        self.music_time = 0
        self.rooms = rooms
        self.ib = None              # the boss index
        self.nb_living_boss = nb_boss
        self.music = music
        self.screen = video
        self.vision = starting_vision
        self.starting_vision = starting_vision
    
    def move (self, coor:tuple, map:list, bosses:list, vags:list, forbiden=())->bool :
        """
        Moves the entity

        input :
            - coor : the coordinates that will increase the current coordinates
            - map : the level representation
            - bosses : a list of the bosses
            - vags : a list of the strays
        output :
            - if we changed our position
        """
        ret = False
        if not self.fighting :                                                                  # normal, he's not fighting
            ret = super ().move (coor, map, self.forbiden_paths)
            # player vs stray
            for vag in vags :
                if (self.coord == vag.get_pos ()) and not vag.is_dead () :
                    print ()
                    print ("***********************")
                    print ("player hit")
                    print ("vag : ", vag.get_health())
                    self.coord = (self.coord[0] - coor[0], self.coord[1] - coor[1])
                    critical = random.random ()
                    if critical > 0.5 :
                        vag.set_health (vag.get_health() - (self.damage * 2))
                    vag.set_health (vag.get_health() - self.damage)
                    print ("vag : ", vag.get_health())
                    self.screen.move_origin ((-coor[0], -coor[1]))                              # if not, the camera move but not the player...
        elif (self.can_play) :                                                                  # he's fighting but he can play
            ret = super ().move (coor, map, self.forbiden_paths)
            self.music.move (coor)
            self.can_play = False
        for i in range (1, len (self.rooms)) :                                                  # starting with 1, 0 is the player starting room
            if (self.coord == self.rooms[i].get_activ_position ()) :                            # we are in a boss activation position
                self.ib = i - 1                                                                 # -1 because of the first room, the player starting room
                self.forbiden_paths.append (self.rooms[i].get_door_position ())
                break
        if (self.ib != None) and not self.fighting :                                            # we juste activate a boss
            self.vision = 3                                                                     # for optimisation
            self.fighting = True
            self.boss = bosses[self.ib]
            self.boss.trigger ()
            self.music.start_fight (self.ib)
            self.music_clock.tick ()
        if (ret) :
            self.screen.move_origin (coor)
        return ret

    def pulse (self, map:list, played:bool) :
        """
        A refresh function called each frame
        you can do what you want here

        input :
            - map : a double array that represents the map of the level (see Level class)
            - played : if we have to resolve the player action
        """
        if self.fighting :
            self.music_time += self.music_clock.tick ()
            if self.have_play and (self.music_time >= ge.Val.TIME_PLAY * ge.Val.MUSIC_TO_TIME) :            # he have to play AND it's the end
                self.have_play = False
                self.can_play = False
                self.music_time = 0
                self.time_wait = self.boss.get_current ()[1]
            elif not self.have_play and (self.music_time >= (self.time_wait - ge.Val.TIME_PLAY) * ge.Val.MUSIC_TO_TIME) :   # he's waiting AND it's the end
                self.have_play = True
                self.can_play = True
                self.music_time = 0
            elif self.boss.is_dead () :                                                                     # ending of the fight
                self.vision = self.starting_vision
                self.fighting = False
                self.music.stop_fight ()
                self.go_to ((self.rooms[self.ib + 1].get_door_position ()), map)                            # +1 because of the first room, the player starting room
                self.forbiden_paths.append (self.rooms[self.ib + 1].get_activ_position ())
                self.boss.lock (self.coord)
                self.ib = None
                self.nb_living_boss -= 1

        if (map[self.coord[1]][self.coord[0]] == " ") :                                                      # void
            self.hp = 0
    
    def is_fighting (self)->bool :
        """
        If the player is fighting against
        a boss

        output :
            - the boolean value
        """
        return self.fighting

    def is_end (self)-> bool :
        """
        If the player has
        beaten all of the bosses
        of the level

        output :
            - the boolean value
        """
        return self.nb_living_boss == 0 or self.is_dead ()

    def go_to (self, coor:tuple, map:list) :
            """
            Changes the position of the entity

            input :
                - coor : the new coordinates
                - map : the level representation
            """
            previous = self.coord
            if (super ().go_to (coor, map)) :
                self.screen.move_origin ((self.coord[0] - previous[0], self.coord[1] - previous[1]))
    
    def get_vision (self)->int :
        """
        Return the range of the player vision
        
        output :
            - the vision range
        """
        return self.vision