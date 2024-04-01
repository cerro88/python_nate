
#libreria
#readchar nos permite leer la entrada del usuario sin necesidad de pulsar intro 
import readchar

#en este caso se usa la libreria os pa ejecutar un comando
import os 


# Se definen estas constantes para que el código sea
# más entendible cuando se tengan que definir esos valores
# más adelante
POST_X = 0 # Índice para la coordenada X en la posición del jugador
POST_Y = 1 # Índice para la coordenada Y en la posición del jugador
MAP_WIDTH = 20 # Ancho del mapa
MAP_HEIGHT = 15 # Alto del mapa
# se inicia la posición en el mapa
my_position = [3, 3] # Posición inicial del jugador en el mapa
while True: # Inicio de un bucle infinito
    # Dibuja el marco superior del mapa
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT): # Bucle para cada fila del mapa
        print("|", end="") # Imprime el borde izquierdo del mapa
        for coordinate_x in range(MAP_WIDTH): # Bucle para cada columna del mapa
            if my_position[POST_X] == coordinate_x and my_position[POST_Y] == coordinate_y:
                print(" @ ", end="") # Imprime la posición del jugador
            else:
                print("   ", end="") # Imprime un espacio vacío
        print("|") # Imprime el borde derecho del mapa y va a la siguiente línea

    # Dibuja el marco inferior del mapa
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Ask user where wants to move
    #direction = input("¿Donde te quieres mover? [WASD]: ")

    #usa la función readchar() del módulo readchar para capturar un único carácter que el usuario teclea sin necesidad de presionar Enter. 
    #Esta función es muy útil en aplicaciones de consola interactivas donde se quiere responder inmediatamente a la entrada del usuario.
    #SE NECESITA IMPORTAR LA LIBRERÍA READCHAR
    direction = readchar.readchar()

    # Si el usuario presiona 'w'
    if direction == "w":
        # Mover hacia arriba reduciendo Y
        my_positon[POST_Y] -= 1
         # Asegurar que la posición Y está dentro de los límites del mapa
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


#comando que se utiliza en programas de Python para limpiar 
    #la pantalla de la consola en sistemas operativos Windows.SE NECESITA IMPORTAR LA LIBRERÍA OS
    #
    os.system("cls")