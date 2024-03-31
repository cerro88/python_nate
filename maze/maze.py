
#libreria
#readchar nos permite leer la entrada del usuario sin necesidad de pulsar intro 
import readchar

#en este caso se usa la libreria os pa ejecutar un comando
import os 


#Se definen estas constantes para que el código sea
#más entendible cuando se tengan que defir esos valores
#más adelante
POST_X = 0
POST_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
#se inicia la posición en el mapa
my_positon = [5, 7]
while True:
    #Dibuja el mapa
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            if my_positon[POST_X] == coordinate_x and my_positon[POST_Y] == coordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Ask user where wants to move
    #direction = input("¿Donde te quieres mover? [WASD]: ")
    direction = readchar.readchar()


    if direction == "w":
        my_positon[POST_Y] -= 1
        my_positon[POST_Y] %= MAP_HEIGHT
    elif direction == "s":
        my_positon[POST_Y] += 1
        my_positon[POST_Y] %= MAP_HEIGHT
        
    elif direction == "a":
        my_positon[POST_X] -= 1
        my_positon[POST_Y] %= MAP_WIDTH
    elif direction == "d":
        my_positon[POST_X] += 1
        my_positon[POST_X] %= MAP_WIDTH
    elif direction == "q":
        break

    os.system("cls")