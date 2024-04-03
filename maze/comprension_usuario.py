
POST_X = 0
POST_Y = 1


MAP_WIDTH = 20
MAP_HEIGHT = 15


my_position = [3 , 3]

#libreria
#readchar nos permite leer la entrada del usuario sin necesidad de pulsar intro 
import readchar

#en este caso se usa la libreria os pa ejecutar un comando
import os 

while True: # Inicio de un bucle infinito
    #dibuja la parte superior
    #dibujará + seguido de tantos guiones como el map_width
    #multiplicado por tres lo que define la anchuna --- de casa casilla
    #finalizando la esquina con +

    #este bucle for recorre el rando de map_height en la coordenada y
    #imprimiendo |, end evita el salto de línea
    #este bucle dibuja la parte izquierda del tablero
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        #dentro otro bucle que recorrerá el rango de map_widht en la coordenada x 
        #imprimiendo tres espacios
        for coordinate_x in range(MAP_WIDTH):
            #el código está comprobando si está en la celda del mapa donde debe estar el jugador. 
            #Si es así, imprime el símbolo del jugador, de lo contrario, imprime espacios vacíos.
            if my_position[POST_X] == coordinate_x and my_position[POST_Y] == coordinate_y:
                    print(" @ ", end="") # Imprime la posición del jugador
            else:
                print("   ", end="")
        #se imprime el borde derecho del tablero
        print("|")

    #dibuja la parte inferior
    #dibujará + seguido de tantos guiones como el map_width
    #multiplicado por tres lo que define la anchuna --- de casa casilla
    #finalizando la esquina con +
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    #usa la función readchar() del módulo readchar para capturar un único carácter que el usuario teclea sin necesidad de presionar Enter. 
        #Esta función es muy útil en aplicaciones de consola interactivas donde se quiere responder inmediatamente a la entrada del usuario.
        #SE NECESITA IMPORTAR LA LIBRERÍA READCHAR
    direction = readchar.readchar()

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
            my_position[POST_Y] %= MAP_WIDTH
    elif direction == "d":
            my_position[POST_X] += 1
            my_position[POST_X] %= MAP_WIDTH
    elif direction == "q":
        break


#comando que se utiliza enprint("+" + "-" * MAP_WIDTH * 3 + "+")

 #programas de Python para limpiar 
    #la pantalla de la consola en sistemas operativos Windows.SE NECESITA IMPORTAR LA LIBRERÍA OS
    
    os.system("cls")