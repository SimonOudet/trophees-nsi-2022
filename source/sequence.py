# -*- coding: utf-8 -*-

import collections as co

class Sequence :
    def __init__ (self) :
        """
        Basic constructor of a Sequence object, basically a double file
        """
        self.actions = co.deque ()
        self.times = co.deque ()
        self.size = 0
    
    def get_actions_time (self)->tuple :
        """
        Get the action and the time of a turn
        
        output :
            - the actions (tuple of Action)
            - the time (int, in ms)
        """
        assert self.size > 0, "the sequence is empty"
        self.size -= 1
        return self.actions.pop ()
    
    def add_actions (self, actions:list, time:int) :
        """
        Add a serie of action

        input :
            - actions : a list with all the actions
            - time : the time in ms
        """
        self.size += 1
        self.actions.appendleft ((actions, time))
    
    def is_empty (self)->bool :
        """
        If the sequence is empty
        
        outtput :
            - the boolean value
        """
        return self.size == 0

class Action :
    def __init__ (self, type:str, dest:list) :
        """
        Basic constructor of an Action object
        
        input :
            - type : the type of the action (D: delet, A: add)
            - dest : the coordinates of the affected case
        """
        self.type = type
        self.dest = dest
    
    def __str__(self) -> str :
        return self.type + " " + str (self.dest)
    
    def get_type (self)->str :
        """
        Get the type of the represented action
        
        output :
            - the type
        """
        return self.type
    
    def get_dest (self)->list :
        """
        Get the destination of the represented action
        
        output :
            - the destination
        """
        return self.dest
