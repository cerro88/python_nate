import readchar
import os
import random

POST_X = 0
POST_Y = 1

MAP_WIDTH = 30
MAP_HEIGHT = 30

my_position = [3, 3]

end_game = False
died = False

#diccionario de trainers
trainers = {
    (4, 6): "entrenador_1",  
    (5, 27): "entrenador_2",
    (10, 16): "entrenador_3",
    (20, 14): "entrenador_4"
}

#Lista para almacenar las coordenadas de los entrenadores visitados
visited_trainers = []

while not end_game:

    while True:

        # Dibujar el mapa
        # Dibuja la parte superior
        print("+" + "-" * MAP_WIDTH * 3 + "+")
        # Este bucle dibuja la parte izquierda del tablero
        for coordinate_y in range(MAP_HEIGHT):
            print("|", end="")

            for coordinate_x in range(MAP_WIDTH):

                char_to_draw = " "
                trainer_in_cell = None

                # Verificar si hay un entrenador en esta celda
                for map_trainer in trainers:
                    if map_trainer[POST_X] == coordinate_x and map_trainer[POST_Y] == coordinate_y:
                        if map_trainer in visited_trainers:
                            # Indica que el entrenador ya ha sido visitado
                            char_to_draw = "V"  
                        else:
                            char_to_draw = "*"
                            trainer_in_cell = map_trainer

                            


                # Verificar si la posición actual es la posición del jugador
                if my_position[POST_X] == coordinate_x and my_position[POST_Y] == coordinate_y:
                    char_to_draw = "&"

                    if trainer_in_cell and trainer_in_cell not in visited_trainers:
                        # Agregar el entrenador a la lista de visitados
                        visited_trainers.append(trainer_in_cell)  

                print(" {} ".format(char_to_draw), end="")
            print("|")

        # Se imprime el borde derecho del tablero
        print("+" + "-" * MAP_WIDTH * 3 + "+")

        direction = readchar.readchar()
        
        new_position = None

        # Si el usuario presiona 'w'
        if direction == "w":
            # Mover hacia arriba reduciendo Y
            my_position[POST_Y] -= 1
            # Asegurar que la posición Y está dentro de los límites del mapa
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
            break
if died:
    print("¡Has muerto!)")
