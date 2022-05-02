# -*- coding: utf-8 -*-

import pygame

class Music :
    def __init__ (self, nb_boss:int, orientations:list):
        self.times_notes = [load_times ("boss", i) for i in range (nb_boss)]        # for all fights, a list of the notes duration
        self.chanels = [pygame.mixer.Channel (i) for i in range (nb_boss)]          # the audio channels, the last is alway the playing channel (you will see)
        self.scales
        self.completed
        self.ib
        self.musics
        self.is_playing
    
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
            times.append (int (ligne))
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
        for i in range (0, len (lignes), 3) :
            x, y = tuple (map (int, lignes[i].rstrip ('\n').split ())) # \n for linux
            if (orientation[0]) :               # we have to switch x and y
                x, y = y, x
            scale[(x * orientation[1][0], y * orientation[1][1])] = lignes[i + 1]
    return scale