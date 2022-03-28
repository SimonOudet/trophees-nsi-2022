
def a_star_path (map:list, src:tuple, dst:tuple)-> list :
    """
    Return the a star path between src and dst

    input :
        - map : the map
        - src : the coordinates of the start
        - dst : the coordinates of the end
    output :
        - the list with all the coordinates
    """
    closed = {src:None}
    open = {}
    a_star (map, src, dst, closed, open)
    return get_path (closed, dst)

def a_star (map:list, src:tuple, dst:tuple, closed:dict, open={}) :
    """
    Find the a star path between src and dst

    input :
        - map : the map
        - src : the coordinates of the start
        - dst : the coordinates of the end
        - closed : the coordinates already check
    """
    if (src == dst) :
        return True
    for node in get_neighbours (src, map) :
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
    if (soon_father[1] == None) : # no way
        return False
    closed[soon_father[0]] = soon_father[1]
    open.pop (soon_father[0])
    return a_star (map, soon_father[0], dst, closed, open)

def get_neighbours (coor:tuple, map:list)-> list :
    """
    Return the neighbours of the given coordinates
    
    input :
        - coor : the coordinates
        - map : the map
    output :
        - a list with all cordinates of all neighbours
    """
    nei = []
    for x in range (coor[0] - 1, coor[0] + 2) :
        for y in range (coor[1] - 1, coor[1] + 2) :
            if ((x, y) != coor) and is_in_map ((x, y), map) :
                nei.append ((x, y))
    return nei

def is_in_map (coor:tuple, map:list)-> bool :
    """
    Return if the given coordinates is in the map
    
    input :
        - coor : the coordinates
        - map : the map
    output :
        - if the given coordinates is in the map
    """
    return (coor[0] >= 0) and (coor[1] >= 0) and (coor[0] < len (map[0])) and (coor[1] < len (map))

def get_quality (src:tuple, test:tuple, dst:tuple)-> int :
    """
    Return the quality of a coordinates
    
    input :
        - src : the sart
        - test : the coordinates to test
        - dst : the end
    output :
        - the quality
    """
    return manathan (test, src) + manathan (test, dst)

def manathan (a:tuple, b:tuple)-> int :
    """
    Return manathan distance between a and b
    
    input :
        - a : the sart
        - b : the test
    output :
        - the distance
    """
    return abs (a[0] - b[0]) + abs (a[1] - b[1])

def get_path (dict:dict, src:tuple)-> list :
    """
    Return the path of the a_star function
    
    input :
        - dict : the dictionnary changed by a_star
        - src : the source
    output :
        - the a star path from src
    """
    if (dict[src] == None) :
        return [src]
    return get_path (dict, dict[src]) + [src]
