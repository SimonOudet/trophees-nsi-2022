# -*- coding: utf-8 -*-

def a_star_path (map:list, src:tuple, dst:tuple)-> list :
    """
    Returns the a star path between src and dst

    input :
        - map : the map
        - src : the coordinates of the starting point
        - dst : the coordinates of the ending point
    output :
        - a list with all the coordinates
    """
    closed = {src:None}
    open = {}
    a_star (map, src, dst, closed, open)
    return get_path (closed, dst) + [dst]

def a_star (map:list, src:tuple, dst:tuple, closed:dict, open={}) :
    """
    Finds the a star path between src and dst

    input :
        - map : the map
        - src : the coordinates of the starting point
        - dst : the coordinates of the ending point
        - closed : the coordinates already checked
    """
    if (src == dst) :
        return True
    for node in get_diag_neighbours (src, map) :
        if (map[node[1]][node[0]] == "#") or (node in closed) :
            continue
        elif (node in open) : # refresh
            q = get_quality (src, node, dst)
            if (q < open[node][0]) :
                open[node] = [q, src]
        else :
            open[node] = [get_quality (src, node, dst), src]
    min = float ("inf") # best quality
    soon_father = (None, None)
    for node in open :
        if (open[node][0] < min) :
            min = open[node][0]
            soon_father = (node, open[node][1])
***    if (soon_father[1] == None) : # no way
        return False
    closed[soon_father[0]] = soon_father[1]
    open.pop (soon_father[0])
    return a_star (map, soon_father[0], dst, closed, open)

def get_neighbours (coor:tuple, map:list)-> list :
    """
    Returns the neighbours of the given coordinates

    input :
        - coor : the coordinates
        - map : the map
    output :
        - a list with all the coordinates of all the neighbours
    """
    nei = []
    for x in [coor[0] - 1, coor[0] + 1] :
        if is_in_map ((x, coor[1]), map) :
            nei.append ((x, coor[1]))
    for y in [coor[1] - 1, coor[1] + 1] :
        if is_in_map ((coor[0], y), map) :
            nei.append ((coor[0], y))
    return nei

def get_diag_neighbours (coor:tuple, map:list)-> list :
    """
    Returns the neighbours of the given coordinates (with diagonals)

    input :
        - coor : the coordinates
        - map : the map
    output :
        - a list with all the coordinates of all the neighbours
    """
    nei = []
    for x in range (coor[0] - 1, coor[0] + 2) :
        for y in range (coor[1] - 1, coor[1] + 2) :
            if ((x, y) != coor) and is_in_map ((x, y), map) :
                nei.append ((x, y))
    return nei

def is_in_map (coor:tuple, map:list)-> bool :
    """
    Returns if the given coordinates are in the map

    input :
        - coor : the coordinates
        - map : the map
    output :
        - True if the given coordinates are in the map, False if they are not
    """
    return (coor[0] >= 0) and (coor[1] >= 0) and (coor[0] < len (map[0])) and (coor[1] < len (map))

def get_quality (src:tuple, test:tuple, dst:tuple)-> int :
    """
    Returns the quality of the given coordinates

    input :
        - src : the starting point
        - test : the coordinates to test
        - dst : the ending point
    output :
        - the quality
    """
    return manatan (test, src) + manatan (test, dst)

def manatan (a:tuple, b:tuple)-> int :
    """
    Returns the manathan distance between a and b

    input :
        - a : the starting point
        - b : the test
    output :
        - the distance
    """
    return abs (a[0] - b[0]) + abs (a[1] - b[1])

def manatan_vision (n:int, map:list, coor:tuple, coors:list, discover:dict, from_blind=False) :
    """
    Returns a list wich represents the vision of the player

    input :
        - n : the manatan width
        - map : the map
        - coor : the root coordinates
        - coors : the coordinates that represent the vision
        - discover : the list of the discovered places
        - from_blind : if the origin is a wall or a door (both of them stop vision)
    """
    discover[coor] = True
    if (coor not in coors) :
        coors.append (coor)
    if (n == 0) or from_blind :
        return
    for ne in get_neighbours (coor, map) :
        if (map[ne[1]][ne[0]] != "#") and (map[ne[1]][ne[0]] != ".") :
            manatan_vision (n - 1, map, ne, coors, discover, False)
        else :
            manatan_vision (n - 1, map, ne, coors, discover, True)

def get_path (dict:dict, src:tuple)-> list :
    """
    Returns the path of the a_star function

    input :
        - dict : the dictionnary changed by a_star
        - src : the source
    output :
        - the a star path from src
    """
    if (dict[src] == None) :
        return [src]
    return get_path (dict, dict[src]) + [src]

def search_drawable (drawables:list, coords:tuple)-> int :
    """
    Search in a given list of Drawable object
    the index of the Drawable with the coords coordinates

    input :
        - drawables : the drawables list
        - coords : the coordinates to find
    output :
        - the index if the object is in drawables, -1 if not
    """
    for i in range (len (drawables)) :
        if (drawables[i].get_pos () == coords) :
            return i
    return -1