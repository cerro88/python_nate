import readchar
import os
import random

POST_X = 0
POST_Y = 1


NUM_OF_MAP_OBJECTS = 11

obstacle_definition = """\
####################
             #######
##########         #
               #####
########      ######
#                  #
###         ########
######      ########
#####              #
#         ##########
###      ###########
#                ###
####            ####
########           #
#              #####\
"""

my_position = [3, 3]
tail_length = 0
tail = []
map_objects = []

end_game = False
died = False

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Bucle principal
while not end_game:

    os.system("cls")
    # Generar objetos aleatorios
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)


    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            # Dibujar la cola
            for tail_part in tail:
                if tail_part[POST_X] == coordinate_x and tail_part[POST_Y] == coordinate_y:
                    char_to_draw = "o"
                    tail_in_cell = tail_part

            # Dibujar objetos
            for map_object in map_objects:
                if map_object[POST_X] == coordinate_x and map_object[POST_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            # Dibujar posición actual
            if my_position[POST_X] == coordinate_x and my_position[POST_Y] == coordinate_y:
                char_to_draw = "0"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell: 
                   end_game = True
                   died = True  

             

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"


            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    

    direction = readchar.readchar()

    
    # Mover la cola
    if direction in ["w", "s", "a", "d"]:
        tail.insert(0, my_position.copy())  # Añade la posición actual al inicio de la cola
        if len(tail) > tail_length:
            tail.pop()  # Elimina el exceso en la cola para mantener el tamaño correcto

    # Actualizar posición
    if direction == "w":
        my_position[POST_Y] -= 1
        my_position[POST_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_position[POST_Y] += 1
        my_position[POST_Y] %= MAP_HEIGHT
    elif direction == "a":
        my_position[POST_X] -= 1
        my_position[POST_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POST_X] += 1
        my_position[POST_X] %= MAP_WIDTH
    elif direction == "q":
        end_game = True

    os.system("cls")

if died:
    print("¡Has muerto!")