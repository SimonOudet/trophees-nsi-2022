# -*- coding: utf-8 -*-

import general
import random

def stage_generator (stage_size:int, table_boss_rooms:list)->list :
    """
    function that generates a stage of the games
    
    input : 
        - stage_size : the bigest size of the square representing the empty stage, the size of the floor must be greater than the maximum width or length of the largest boss room
        - table_boss_rooms : table containing each boss room, without the walls, that the floor will contain. 
            Each element of the table will be an table containing the data allowing the 
            generation of a boss room
            [  
              [["v", "g", ...], ["v", "g", ...], ...]->matrix_representing_a_boss_room_with_"v"_for_void_"g"_for_ground_"b"_for_boss_position_and_"p"_for_player’s_departure_position, 
              , ...]
            
            example:
                table_boss_rooms = [[["v", "v", "v", "g", "v"], ["v", "g", "g", "g", "g"], ["g", "g", "g", "g", "v"], ["v", "g", "p", "g", "v"]]]
    
    output : 
        - a double-entry table representing a floor, whose boss rooms are accessible and 
          randomly generated on the floor
        - boss_position = [(x, y), ...]

    """
    rooms = []
    stage = [[" "] * (stage_size * 2) for i in range (stage_size * 2)]

    # placement and creation of each room
    for boss_room in table_boss_rooms :
        rooms.append (general.Room ())                                                      # this object represent the room data       
        compass = random.choice(["north", "south", "east", "west"])                         # random orientation choice
        #print(compass)
        # creation of the room
        if (compass == "north") :
            # 180 degres
            rooms[-1].set_orientation ((False, (-1, -1)))
            new_boss_room = [[None] * len (boss_room[i]) for i in range (len (boss_room))]  # the boss room array, 180 degres = same dimenssion
            for line in range (len (boss_room)) :
                for column in range (len (boss_room[line])) :
                    new_boss_room[len (boss_room) - 1 - line][len (boss_room[line]) - 1 - column] = boss_room[line][column]
        
        elif (compass == "east") :
            # 90 degres
            rooms[-1].set_orientation ((True, (1, -1)))
            new_boss_room = [[None] * len (boss_room) for i in range (len (boss_room[0]))] # 90 degres = swap the width and the height
            for line in range (len (boss_room)) :
                for column in range (len (boss_room[line])) :
                    new_boss_room[len (boss_room[line]) - 1 - column][line] = boss_room[line][column]
        
        elif (compass == "west") :
            # 270 degres
            rooms[-1].set_orientation ((True, (-1, 1)))
            new_boss_room = [[None] * len (boss_room) for i in range (len (boss_room[0]))] # 270 degres = swap the width and the height
            for line in range (len (boss_room)) :
                for column in range (len (boss_room[line])) :
                    new_boss_room[column][len (boss_room) - 1 - line] = boss_room[line][column]
        
        else :
            # 0 or 360 degres
            rooms[-1].set_orientation ((False, (1, 1)))
            new_boss_room = boss_room
        
        # placement of the room

        # searching of a whole place
        x_starting = random.randint (4, (stage_size + 4))
        y_starting = random.randint (4, (stage_size + 4))
        
        while not (colision_test (new_boss_room, stage, x_starting, y_starting)) :
            x_starting += 1
            y_starting += 1
            if (x_starting > stage_size + 4) :
                x_starting = random.randint (4, (stage_size + 4))
            if (y_starting > stage_size + 4) :
                y_starting = random.randint (4, (stage_size + 4))
        
        # placement
        room_generator (new_boss_room, stage, x_starting, y_starting, rooms)
        #for elt in stage :
            #print (elt)
        #print ("")
    
    # switching the doormate to void
    for line_stage in range (len (stage)) :
        for column_stage in range (len (stage[line_stage])) :
            if (stage[line_stage][column_stage] == "M") :
                stage[line_stage][column_stage] = " "
            #print (stage[line_stage][column_stage], end=" ")
        #print("")
    
    # creation of the paths
    family = {rooms[i].get_door_position ():i for i in range (len (rooms))}
    while sum(family.values()) != 0 :                                                       # while each rooms are not in the same family
        departur_door = rooms[random.randint(0, len(rooms) - 1)].get_door_position ()       # starting room
        door_index = random.randint(0, len(rooms) - 1)
        finish_door = rooms[door_index].get_door_position ()                                # ending room
        while (family[finish_door] == family[departur_door]) :                              # if the starting and the ending room are frome the same family 
            door_index += 1
            if (door_index >= len (rooms)) :
                door_index = 0
            finish_door = rooms[door_index].get_door_position ()
        path (stage, finish_door[0], finish_door[1], departur_door[0], departur_door[1])    # creation of the path
        for position in range (len (rooms)) :                                               # all the soons of departur_door and finish_door cone from the same family
            if (family[rooms[position].get_door_position ()] == max (family[departur_door], family[finish_door])) :
                family[rooms[position].get_door_position ()] = min (family[departur_door], family[finish_door])
    
    # creation of the wall
    for line_stage in range (len (stage)) :
        for column_stage in range (len (stage[line_stage])) :
            if (stage[line_stage][column_stage] == "_") :
                # a 3 * 3 square
                for i in range (-1, 2) :
                    for j in range (-1, 2) :
                        if (stage[line_stage + i][column_stage + j] == " ") :
                            stage[line_stage + i][column_stage + j] = "#"
    
    #for line_stage in range (len (stage)) :
    #    for column_stage in range (len (stage[line_stage])) :
    #        print (stage[line_stage][column_stage], end=" ")
    #    print("")
    
    return stage, rooms

def colision_test (boss_rooms:list, stage:list, x_starting_coordinate:int, y_starting_coordinate:int) :
    """
    function that checks if the boss's room to generate meets colision
    
    input :
        - boss_rooms : it's the matrice that represent the boss room
        - stage : this is the stage that the function will modify 
        - x_starting_coordinate,  y_starting_coordinate : the angle coordinate of the boss room
        
    output :
        - True or False : if the boss room that we want to generate meets colision
    """
    for line in range (len (boss_rooms)) :
        for column in range (len (boss_rooms[line])) :
            # if this coordinate is not void AND if it's problematic
            if (stage[line + y_starting_coordinate][column + x_starting_coordinate] != " ") and (boss_rooms[line][column] != " "):
                return False
    return True

def room_generator (boss_rooms:list, stage:list, x_starting_coordinate:int, y_starting_coordinate:int, rooms:general.Room) :
    """
    function that generates a boss room on the stage
    
    input :
        - boss_rooms : it's the matrice that represent the boss room
        - stage : this is the stage that the function will modify 
        - x_starting_coordinate,  y_starting_coordinate : the angle coordinate of the boss room
        - boss_position see function stage_generator
        - door_position see function stage_generator
    """
    for line in range (len (boss_rooms)) :
        for column in range (len (boss_rooms[line])) :
            if (stage[line + y_starting_coordinate][column + x_starting_coordinate] == " ") and (boss_rooms[line][column] != " ") :
                stage[line + y_starting_coordinate][column + x_starting_coordinate] = boss_rooms[line][column]
            if (stage[line + y_starting_coordinate][column + x_starting_coordinate] == "B") :
                rooms[-1].set_boss_position ((column + x_starting_coordinate, line + y_starting_coordinate))
            elif (stage[line + y_starting_coordinate][column + x_starting_coordinate] == ".") :
                rooms[-1].set_door_position ((column + x_starting_coordinate, line + y_starting_coordinate))
            elif (stage[line + y_starting_coordinate][column + x_starting_coordinate] == "-") :
                rooms[-1].set_activ_position ((column + x_starting_coordinate, line + y_starting_coordinate))

def path (stage:list, x_finish_position:int, y_finish_position:int, x_departur_position:int, y_departur_position:int) :
    """
    
    """
    if (x_departur_position == x_finish_position) and (y_departur_position == y_finish_position) :
        return
    x_ideal = x_finish_position - x_departur_position
    y_ideal = y_finish_position - y_departur_position
    ideals = []
    not_ideals = []
    
    if (x_departur_position <= 1) :
        ideals.append((1, 0))
    elif (x_departur_position >= (len (stage) - 1)) :
        ideals.append((-1, 0))
    elif (x_ideal > 0) :
        ideals.append ((1, 0))
        not_ideals.append ((-1, 0))
    elif (x_ideal < 0) :
        ideals.append ((-1, 0))
        not_ideals.append ((1, 0))
    else :
        not_ideals.extend ([(1, 0), (-1, 0)])
    
    if (y_departur_position <= 1) :
        ideals.append((0, 1))
    elif (y_departur_position >= (len (stage[0]) - 1)) :
        ideals.append((0, -1))
    elif (y_ideal > 0) :
        ideals.append ((0, 1))
        not_ideals.append ((0, -1))
    elif (y_ideal < 0) :
        ideals.append ((0, -1))
        not_ideals.append ((0, 1))
    else :
        not_ideals.extend ([(0, 1), (0, -1)])
    
    random.shuffle (ideals)
    random.shuffle (not_ideals)
    path_posibility = ideals + not_ideals
    
    for posibility in path_posibility :
        x = x_departur_position + posibility[0]
        y = y_departur_position + posibility[1]
        if (stage[y][x] == "_") :
            #for line_stage in range (len (stage)) :
                #for column_stage in range (len (stage[line_stage])) :
                    #print (stage[line_stage][column_stage], end=" ")
                #print("")
            return path(stage, x, y, x_finish_position, y_finish_position)
        if (stage[y][x] == " ") :
            stage[y][x] = "_"
            return path(stage, x, y, x_finish_position, y_finish_position)
       
     

########principal########

if __name__ == "__main__" :
    #size = 6
    #table = [[[" ", "#", " ", "#"], [" ", "#", "#", "#"], ["#", "#", " ", "#"]], [["#", " ", "#"], [" ", "#", "#"], ["#", " ", "#"]], [["#", " ", "#"], [" ", "#", "#"], ["#", " ", "#"], ["#", "#", " "]]]
    #for this test the size must biger than 4.
    #size = 18 * 2
    size = 23 * 2
    # " " = void, "#" = wall, "." = door, "M" = doormat, "-" = ground, "B" = boss, "_" = path
    '''
    table = [
        [
        ["#", "#", "#", "#", "#"], 
        ["#", "-", "B", "-", "#"], 
        ["#", "-", "-", "-", "#"], 
        ["#", "-", "-", "-", "#"], 
        ["#", "#", ".", "#", "#"], 
        ["M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M", "M"], 
        ["#", "#", "#", "#", ".", "#", "#"], 
        ["#", "-", "-", "-", "-", "-", "#"], 
        ["#", "B", "-", "-", "-", "-", "#"], 
        ["#", "#", "#", "#", "#", "#", "#"]
        ], 
        [
        [" ", "#", "#", "#", "M"], 
        ["#", "#", "-", "#", "M"], 
        ["#", "-", "-", ".", "M"], 
        ["#", "#", "B", "#", "M"], 
        [" ", "#", "#", "#", "M"]
        ], 
        [
        ["#", "#", "#", "#", "#"], 
        ["#", "B", "-", "-", "#"], 
        ["#", "-", "-", "-", "#"], 
        ["#", "-", "-", "-", "#"], 
        ["#", "#", ".", "#", "#"], 
        ["M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M", "M"], 
        ["#", "#", "#", "#", ".", "#", "#"], 
        ["#", "B", "-", "-", "-", "-", "#"], 
        ["#", "-", "-", "-", "-", "-", "#"], 
        ["#", "#", "#", "#", "#", "#", "#"]
        ], 
        [
        [" ", "#", "#", "#", "M"], 
        ["#", "#", "-", "#", "M"], 
        ["#", "B", "-", ".", "M"], 
        ["#", "#", "-", "#", "M"], 
        [" ", "#", "#", "#", "M"]
        ]
        ]
    '''
    table = [
        [
        ["M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", "#", "M"], 
        ["M", "#", "-", "B", "-", "#", "M"], 
        ["M", "#", "-", "-", "-", "#", "M"], 
        ["M", "#", "-", "-", "-", "#", "M"], 
        ["M", "#", "#", ".", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", ".", "#", "#", "M"], 
        ["M", "#", "-", "-", "-", "-", "-", "#", "M"], 
        ["M", "#", "B", "-", "-", "-", "-", "#", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M"], 
        ["M", " ", "#", "#", "#", "M"], 
        ["M", "#", "#", "-", "#", "M"], 
        ["M", "#", "-", "-", ".", "M"], 
        ["M", "#", "#", "B", "#", "M"], 
        ["M", " ", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", "#", "M"], 
        ["M", "#", "-", "B", "-", "#", "M"], 
        ["M", "#", "-", "-", "-", "#", "M"], 
        ["M", "#", "-", "-", "-", "#", "M"], 
        ["M", "#", "#", ".", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"], 
        ["M", "#", "#", "#", "#", ".", "#", "#", "M"], 
        ["M", "#", "-", "-", "-", "-", "-", "#", "M"], 
        ["M", "#", "B", "-", "-", "-", "-", "#", "M"], 
        ["M", "#", "#", "#", "#", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M", "M", "M", "M"]
        ], 
        [
        ["M", "M", "M", "M", "M", "M"], 
        ["M", " ", "#", "#", "#", "M"], 
        ["M", "#", "#", "-", "#", "M"], 
        ["M", "#", "-", "-", ".", "M"], 
        ["M", "#", "#", "B", "#", "M"], 
        ["M", " ", "#", "#", "#", "M"], 
        ["M", "M", "M", "M", "M", "M"]
        ]
        ]
    stage_generator (size, table)
