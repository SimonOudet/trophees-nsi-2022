# -*- coding: utf-8 -*-

def is_in_square (center:tuple, n:int, coor:tuple, add=False, dict=None)->bool :
    """
    Check if a given position
    is in a virtual square
    
    input :
        - center : the center coordinates of the square
        - n : the width and height of the square
        - coor : the coordiates to test
        - add : special flag, don't care
        - dict : same
    output :
        - if the given position is in the square
    """
    rep = (coor[0] >= center[0] - n // 2) and (coor[0] <= center[0] + n // 2) and (coor[1] >= center[1] - n // 2) and (coor[1] <= center[1] + n // 2)
    if (rep and add) :
        dict[coor] = True
    return rep