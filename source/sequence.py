# -*- coding: utf-8 -*-

class Sequence :
    def __init__ (self, actions:list, times:list) :
        """
        Basic constructor of a Sequence object
        
        input :
            - actions : a list of actions
            - times : the list of times (ms) for each action
        """
        self.actions = actions
        self.times = times
        self.i = -1
    
    def get_action_time (self)->tuple :
        """
        Get the action and the time of a turn
        
        output :
            - the action
            - the time
        """
        self.i += 1
        return self.actions[self.i], self.times[self.i]

class Action :
    def __init__ (self, type:str, dest:list) :
        """
        Basic constructor of an Action object
        
        input :
            - type : the type of the action (M: move, A: attack)
            - dest : the coordinates of the destination in the case of a moving, or the coordinates of the affected case in the case of an attack
        """
        self.type = type
        self.dest = dest
    
    def get_type (self)->str :
        """
        Get the type of the represented action
        
        output :
            - the type
        """
        return self.type
    
    def get_dest (self)->list :
        """
        Get the destination(s) of the represented action
        
        output :
            - the destination(s)
        """
        return self.dest
