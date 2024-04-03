import readchar
import os
import random

POST_X = 0
POST_Y = 1

MAP_WIDTH = 20
MAP_HEIGHT = 15
#
NUM_OF_MAP_OBJECTS = 11

my_position = [3 , 3]

#
map_objects = []

#generar random objetos

while len(map_objects) < (NUM_OF_MAP_OBJECTS):
    new_position = ([random.randint(0,MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)])

    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)




#bucle principal
while True:
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            chard_to_draw = " "
            #
            object_in_cell = None

            #
            for map_object in map_objects:
                #
                if map_object[POST_X] == coordinate_x and map_object[POST_Y] == coordinate_y:
                    #
                    chard_to_draw = "*"
                    #
                    object_in_cell = map_object


            if my_position[POST_X] == coordinate_x and my_position[POST_Y] == coordinate_y:
                #
                chard_to_draw = "@" 

                #
                #
                if object_in_cell:
                    map_objects.remove(object_in_cell)


                #
            print(" {} ".format(chard_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")


    direction = readchar.readchar()

    if direction == "w":
        my_position[POST_Y] -= 1
        my_position[POST_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POST_Y] += 1
        my_position[POST_Y] %= MAP_HEIGHT
        
    elif direction == "a":
        my_position[POST_X] -= 1
        my_position[POST_Y] %= MAP_WIDTH
    elif direction == "d":
        my_position[POST_X] += 1
        my_position[POST_X] %= MAP_WIDTH
    elif direction == "q":
        break



    os.system("cls")