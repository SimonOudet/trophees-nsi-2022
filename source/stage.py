# -*- coding: utf-8 -*-

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
                table_boss_rooms = [([["v", "v", "v", "g", "v"], ["v", "g", "g", "g", "g"], ["g", "g", "g", "g", "v"], ["v", "g", "p", "g", "v"]])]
    
    output : 
        - a double-entry table representing a floor, whose boss rooms are accessible and 
            randomly generated on the floor

    """ 
    stage = [[" "] * (stage_size * 2) for i in range (stage_size * 2)]
    for boss_room in table_boss_rooms :
        compass = random.choice(["north", "south", "east", "west"])
        #print(compass)
        if (compass == "north") :
            new_boss_room = [[None] * len (boss_room[i]) for i in range (len (boss_room))]
            for line in range (len (boss_room)) :
                for column in range (len (boss_room[line])) :
                    new_boss_room[len (boss_room) - 1 - line][len (boss_room[line]) - 1 - column] = boss_room[line][column]
        
        elif (compass == "east") :
            new_boss_room = [[None] * len (boss_room) for i in range (len (boss_room[0]))]
            for line in range (len (boss_room)) :
                for column in range (len (boss_room[line])) :
                    new_boss_room[len (boss_room[line]) - 1 - column][line] = boss_room[line][column]
        
        elif (compass == "west") :
            new_boss_room = [[None] * len (boss_room) for i in range (len (boss_room[0]))]
            for line in range (len (boss_room)) :
                for column in range (len (boss_room[line])) :
                    new_boss_room[column][len (boss_room) - 1 - line] = boss_room[line][column]
        
        else :
            new_boss_room = boss_room
        
        x_starting = random.randint (0, stage_size)
        y_starting = random.randint (0, stage_size)
        
        while not (colision_test (new_boss_room, stage, x_starting, y_starting)) :
            x_starting += 1
            y_starting += 1
            if (x_starting > stage_size) :
                x_starting = random.randint (0, stage_size)
            if (y_starting > stage_size) :
                y_starting = random.randint (0, stage_size)
        
        room_generator (new_boss_room, stage, x_starting, y_starting)
        #for elt in stage :
            #print (elt)
        #print ("")
        
    for line_stage in range (len (stage)) :
        for column_stage in range (len (stage[line_stage])) :
            if (stage[line_stage][column_stage] == "M") :
                stage[line_stage][column_stage] = " "
            print (stage[line_stage][column_stage], end=" ")
        print("")

def colision_test (boss_rooms:list, stage:list, x_starting_coordinate:int, y_starting_coordinate:int) :
    """
    function that checks if the boss’s room to generate meets colision
    
    input :
        - boss_rooms : it's the matrice that represent the boss room
        - stage : this is the stage that the function will modify 
        - x_starting_coordinate,  y_starting_coordinate : the angle coordinate of the boss room
        
    output :
        - True or False : if the boss room that we want to generate meets colision
    """
    for line in range (len (boss_rooms)) :
        for column in range (len (boss_rooms[line])) :
            if (stage[line + x_starting_coordinate][column + y_starting_coordinate] != " ") and (boss_rooms[line][column] != " "):
                return False
    return True

def room_generator (boss_rooms:list, stage:list, x_starting_coordinate:int, y_starting_coordinate:int) :
    """
    function that generates a boss room on the stage
    
    input :
        - boss_rooms : it's the matrice that represent the boss room
        - stage : this is the stage that the function will modify 
        - x_starting_coordinate,  y_starting_coordinate : the angle coordinate of the boss room
    """
    for line in range (len (boss_rooms)) :
        for column in range (len (boss_rooms[line])) :
            if (stage[line + x_starting_coordinate][column + y_starting_coordinate] == " ") and (boss_rooms[line][column] != " "):
                stage[line + x_starting_coordinate][column + y_starting_coordinate] = boss_rooms[line][column]

def path () :
    """
    
    """
    pass

########principal########

#size = 6
#table = [[[" ", "#", " ", "#"], [" ", "#", "#", "#"], ["#", "#", " ", "#"]], [["#", " ", "#"], [" ", "#", "#"], ["#", " ", "#"]], [["#", " ", "#"], [" ", "#", "#"], ["#", " ", "#"], ["#", "#", " "]]]
#for this test the size must biger than 4.
size = 18 * 2
# " " = void, "#" = wall, "." = door, "M" = doormat, "-" = ground
table = [
    [
     ["#", "#", "#", "#", "#"], 
     ["#", "-", "-", "-", "#"], 
     ["#", "-", "-", "-", "#"], 
     ["#", "-", "-", "-", "#"], 
     ["#", "#", ".", "#", "#"], 
     ["M", "M", "M", "M", "M"]
     ], 
    [
     ["M", "M", "M", "M", "M", "M", "M"], 
     ["#", "#", "#", "#", ".", "#", "#"], 
     ["#", "-", "-", "-", "-", "-", "#"], 
     ["#", "-", "-", "-", "-", "-", "#"], 
     ["#", "#", "#", "#", "#", "#", "#"]
     ], 
    [
     [" ", "#", "#", "#", "M"], 
     ["#", "#", "-", "#", "M"], 
     ["#", "-", "-", ".", "M"], 
     ["#", "#", "-", "#", "M"], 
     [" ", "#", "#", "#", "M"]
     ], 
    [
     ["#", "#", "#", "#", "#"], 
     ["#", "-", "-", "-", "#"], 
     ["#", "-", "-", "-", "#"], 
     ["#", "-", "-", "-", "#"], 
     ["#", "#", ".", "#", "#"], 
     ["M", "M", "M", "M", "M"]
     ], 
    [
     ["M", "M", "M", "M", "M", "M", "M"], 
     ["#", "#", "#", "#", ".", "#", "#"], 
     ["#", "-", "-", "-", "-", "-", "#"], 
     ["#", "-", "-", "-", "-", "-", "#"], 
     ["#", "#", "#", "#", "#", "#", "#"]
     ], 
    [
     [" ", "#", "#", "#", "M"], 
     ["#", "#", "-", "#", "M"], 
     ["#", "-", "-", ".", "M"], 
     ["#", "#", "-", "#", "M"], 
     [" ", "#", "#", "#", "M"]
     ]
    ]
stage_generator (size, table)
