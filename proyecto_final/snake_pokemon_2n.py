#¡FINAL BOSS!
#
#El objetivo de este ejercicio final es crear un desafío Pokémon (o lo que más os guste/motive). 
#Cada uno de los objetos será un entrenador pokémon, cuando nos situamos encima de una casilla que contiene un objeto, 
#se lanzará un combate pokémon para luchar contra el entrenador rival. Tenemos que ganar el combate para que el entrenador 
#desaparezca de nuestra lista e ir sucesivamente ganando a cada entrenador (objeto). Cuando hayamos vencido, se terminará el juego.
#
#Nuestro pokémon será Pikachu y cada entrenador tendrá un solo pokémon a libre elección y con los ataques que queráis.


#biblioteca readchar para leer caracteres 
#de entrada sin necesidad de presionar Enter.
import readchar
# biblioteca os para 
#interactuar con el sistema operativo.
import os
# biblioteca random para generar números aleatorios.
import random
#funciones que permiten manejar la entrada y salida en Windows.
import msvcrt

#Constantes 
#para representar las posiciones 'x' y 'y' en las coordenadas.
POST_X = 0
POST_Y = 1

#Dimensiones del mapa del juego
MAP_WIDTH = 30
MAP_HEIGHT = 30

#Posición inicial del jugador en el mapa
my_position = [3, 3]

#variables de control para el estado del juego
#Controla si el juego debe terminar
end_game = False
#Indica si el jugador ha perdido
game_over = False

#diccionario de trainers y sus coordenadas
trainers = {
    (4, 6): {"name": "entrenador_1", "pokemon": "Squirtle", "vida": 90, "ataques": {"Placaje": 10, "Pistola Agua": 15, "Burbuja": 8}},
    (5, 27): {"name": "entrenador_2", "pokemon": "Charmander", "vida": 85, "ataques": {"Lanzallamas": 18, "Ascuas": 12}},
    (10, 16): {"name": "entrenador_3", "pokemon": "Bulbasaur", "vida": 90, "ataques": {"Latigazo": 13, "Hoja Afilada": 16}},
    (20, 14): {"name": "entrenador_4", "pokemon": "Jigglypuff", "vida": 95, "ataques": {"Canto": 0, "Golpe Cuerpo": 10}}
}
#Lista para almacenar las coordenadas de los 
#entrenadores visitados
visited_trainers = []

#Bucle principal del juego 
#continúa hasta que el juego termine o el jugador pierda.
while not end_game and not game_over:
    #Bucle para redibujar el mapa cada 
    #vez que ocurre un evento (como un movimiento)
    while True:

        # Dibujar el mapa
        # Dibuja la parte superior
        print("+" + "-" * MAP_WIDTH * 3 + "+")
        #Este bucle dibuja cada fila del mapa
        for coordinate_y in range(MAP_HEIGHT):
            #Inicia la línea del mapa con un borde vertical
            print("|", end="")

            #Bucle para cada celda en la fila actual
            for coordinate_x in range(MAP_WIDTH):
                #Carácter por defecto para celdas vacías
                draw = " "
                #Variable para guardar si hay un entrenador en la celda
                trainer_in_cell = None

                # Verificar si hay un entrenador en la celda
                for trainer in trainers:
                    if trainer[POST_X] == coordinate_x and trainer[POST_Y] == coordinate_y:
                        if trainer in visited_trainers:
                            # Indica que el entrenador ya ha sido visitado
                            draw = "V"  
                        else:
                            draw = "*"
                            #si el entrenador no ha sido visitado se asigna a esa celda
                            trainer_in_cell = trainer

                            


                #Verifica si la posición actual es la posición del jugador
                if my_position[POST_X] == coordinate_x and my_position[POST_Y] == coordinate_y:
                    draw = "&"

                    if trainer_in_cell and trainer_in_cell not in visited_trainers:
                        #Si el jugador está en la misma celda que 
                        #un entrenador no visitado, lo agrega a visitados
                        visited_trainers.append(trainer_in_cell)  
                # Imprime el carácter de la celda actual 
                #y continúa en la misma línea
                print(" {} ".format(draw), end="")
             #Finaliza la línea del mapa con un borde vertical
            print("|")

        # Se imprime el borde derecho del tablero
        print("+" + "-" * MAP_WIDTH * 3 + "+")

        #Lee un carácter del teclado, 
        #que representa la dirección de movimiento del jugador
        direction = readchar.readchar()
        #variable para la nueva posición del jugador, que será calculada
        new_position = None

        #Si el usuario presiona 'w'
        if direction == "w":
            # Mover hacia arriba reduciendo Y
            my_position[POST_Y] -= 1
            # Asegurar que la posición Y está dentro de los límites del mapa, usando módulo para ciclar al otro extremo si necesario
            my_position[POST_Y] %= MAP_HEIGHT
        #Si el usuario presiona 's'
        elif direction == "s":
            # Mover hacia abajo aumentando Y
            my_position[POST_Y] += 1
            # Asegurar que la posición Y está dentro de los límites del mapa, similar al movimiento hacia arriba
            my_position[POST_Y] %= MAP_HEIGHT

        elif direction == "a":
            #Mover hacia la izquierda reduciendo X
            my_position[POST_X] -= 1
            #Asegurar que la posición X está dentro de los límites del mapa
            my_position[POST_X] %= MAP_WIDTH

        elif direction == "d":
            #Mover hacia la derecha aumentando X
            my_position[POST_X] += 1
            #Asegurar que la posición X está dentro de los límites del mapa
            my_position[POST_X] %= MAP_WIDTH
        #Si el usuario presiona 'q'
        elif direction == "q":
            #Salir del bucle, lo que puede significar pausar o terminar el juego
            break

        if tuple(my_position) in trainers:
            trainer = trainers[tuple(my_position)]
            print(f"¡Has encontrado a {trainer['name']} con su Pokémon {trainer['pokemon']}! ¡Prepárate para el combate!")
            input("Presiona Enter para continuar...")

            # Inicia variables de vida para el combate
            pikachu_life = 90  # Vida inicial de Pikachu
            opponent_life = trainer['vida']  # Vida inicial del Pokémon oponente

            while pikachu_life > 0 and opponent_life > 0:
                # Turno del Pokémon oponente
                print(f"Turno de {trainer['pokemon']}")
                ataque_oponente = random.choice(list(trainer['ataques'].keys()))
                dano = trainer['ataques'][ataque_oponente]
                pikachu_life -= dano
                print(f"{trainer['pokemon']} ataca con {ataque_oponente} causando {dano} puntos de daño")

                # Mostrar la vida actualizada
                print(f"Vida de {trainer['pokemon']}: {'#' * (opponent_life // 10)}, vida de Pikachu: {'#' * (pikachu_life // 10)}")
                msvcrt.getch()
                os.system("cls")

                # Turno de Pikachu
                print("Turno de Pikachu")
                print("Selecciona tu ataque:")
                print("1. Bola Voltio")
                print("2. Onda Trueno")
                print("3. Chispa")
                choice = msvcrt.getch().decode()

                if choice == "1":
                    opponent_life -= 10
                    print("Pikachu ataca con Bola Voltio")
                elif choice == "2":
                    opponent_life -= 12
                    print("Pikachu ataca con Onda Trueno")
                elif choice == "3":
                    opponent_life -= 5
                    print("Pikachu ataca con Chispa")
                else:
                    print("Opción no válida. Por favor, selecciona un número del 1 al 3.")

                # Mostrar la vida actualizada
                print(f"Vida de {trainer['pokemon']}: {'#' * (opponent_life // 10)}, vida de Pikachu: {'#' * (pikachu_life // 10)}")
                msvcrt.getch()
                os.system

                # Determinar el resultado del combate
                if pikachu_life <= 0:
                    print("¡El oponente gana!")
                    # Marca el juego como terminado si el oponente gana
                    game_over = True
                    # Muestra mensaje de Game Over y termina el juego
                    print("Game Over: Pikachu ha sido derrotado.")
                elif opponent_life <= 0:
                    print("¡Has ganado!")
                    # Elimina al entrenador derrotado del mapa
                    del trainers[tuple(my_position)]
                    # Mensaje de victoria específico
                    print(f"¡Has derrotado a {trainer['name']} y su {trainer['pokemon']}!")

                # Verifica si el juego debe terminar
                if game_over:
                    print("El juego ha terminado. Gracias por jugar.")
                    break  # Termina el bucle principal y finaliza el juegoo
            