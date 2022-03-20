
def is_in_square (center:tuple, n:int, coor:tuple, add=False, dict=None)->bool :
    """
    Check if a given position
    is in a virtual square
    
    input : - center : the center coordinates of the square \n
            - n : the width and height of the square \n
            - coor : the coordiates to test \n
            - add : special flag, don't care \n
            - dict : same \n
    output : - if the given position is in the square
    """
    rep = (coor[0] >= center[0] - n // 2) and (coor[0] <= center[0] + n // 2) and (coor[1] >= center[1] - n // 2) and (coor[1] <= center[1] + n // 2)
    if (rep and add) :
        dict[coor] = True
    return rep