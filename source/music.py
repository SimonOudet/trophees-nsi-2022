# -*- coding: utf-8 -*-

import general as ge
import pulsable
import pygame

class Music (pulsable.Pulsable) :
    def __init__ (self, nb_boss:int, orientations:list):
        """
        Basic constructor of a Music object,
        the music manager of the game
        
        input :
            - nb_boss : the number of bosses of the level
            - orientations : a list of all the orientation of the boss rooms
        """
        self.times_notes = [load_times ("boss", i) for i in range (nb_boss)]                        # for all fights, a list of the notes duration
        self.chanels = [pygame.mixer.Channel (i) for i in range (nb_boss)]                          # the audio channels, the last is alway the playing channel (you will see)
        self.scales = [load_scale ("boss", i, orientations[i]) for i in range (nb_boss)]            # the scales, dictionnarys movement->Sound
        self.completed = [False for i in range (nb_boss)]
        self.ib = None
        self.musics = [pygame.mixer.Sound ("data/musics/boss" + str (i) + ".wav") for i in range (nb_boss)]
        self.music_clock = pygame.time.Clock ()
        self.music_time = 0
        self.inote = -1                                                                             # the note index
    
    def pulse (self, map:list, played:bool) :
        """
        Manage the duration of each note
        input are not used here
        
        input :
            - map : a double array wich represent a map of the level (see Level class)
            - played : if we have to resolve the player action
        """
        if (self.ib != None) :                                                                      # the player is fighting
            self.music_time += self.music_clock.tick ()
            if (self.music_time * ge.Val.MUSIC_TO_TIME >= self.times_notes[self.ib][self.inote]) :  # end of the current sound
                self.chanels[-1].stop ()                                                            # the last channel is the player channel

    def start_fight (self, ib:int) :
        """
        Sart a music fight
        
        input :
            - ib : the boss id
        """
        self.ib = ib
        to_start = [i for i in range (len(self.musics)) if self.completed[i]]                       # the audio already complet
        for i in range (len (to_start)) :
            self.chanels[i].play (self.musics[to_start[i]])
    
    def stop_fight (self) :
        """
        Stop the music fight
        """
        pygame.mixer.stop ()
        self.completed[self.ib] = True
        self.ib = None
        self.inote = -1
    
    def move (self, direction:tuple) :
        """
        The player has moved in this direction

        input :
            direction : the player moving direction
        """
        if (self.ib != None) :
            self.inote += 1
            self.chanels[-1].play (self.scales[self.ib][direction])
    
def load_times (name:str, i:int)->list :
    """
    Load, from a txt file, a time list
    
    input :
        - name : the name of the file (boss for a boss...)
        - i : the index
    output :
        - the time list
    """
    times = []
    with open ('data/notes_times/' + name + str (i) + '.txt','r') as fichier :
        # for linux :
        for ligne in fichier :
            ligne = ligne.rstrip ('\n')
            times.append (int (ligne)) #  - ge.Val.TIME_PLAY removing the time to play for translate from note time to boss thinking time
    return times

def load_scale (name:str, i:int, orientation:tuple)->dict :
    """
    Load, from a txt file, a scale (a dictionnary movement->Sound)
    
    input :
        - name : the name of the file (boss for a boss...)
        - i : the index
        - orientation : the orientation (a tuple with : (if we have to switch x and y, a tupple for the coordinates)
    output :
        - the scale dictionnary
    """
    scale = {}
    with open ('data/scales/' + name + str (i) + '.txt','r') as fichier :
        lignes = fichier.readlines ()
        for l in range (0, len (lignes), 3) :
            x, y = tuple (map (int, lignes[l].rstrip ('\n').split ()))                               
            if (orientation[0]) :                                                                                                                           # we have to switch x and y
                x, y = y, x                                                       # \n for linux
            scale[(x * orientation[1][0], y * orientation[1][1])] = pygame.mixer.Sound ("data/sound/boss" + str (i) + "/" + lignes[l + 1].rstrip ('\n').split ()[0] + ".wav") # \n for linux, again
    return scale
