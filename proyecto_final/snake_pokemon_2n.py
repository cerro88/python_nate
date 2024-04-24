
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
    (4, 6): "entrenador_1",  
    (5, 27): "entrenador_2",
    (10, 16): "entrenador_3",
    (20, 14): "entrenador_4"
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

        # Verifica si la posición actual del jugador coincide con la de algún entrenador
        if tuple(my_position) in trainers:
            #Recupera el nombre del entrenador en la posición actual
            trainer_name = trainers[tuple(my_position)]
            #Informa al jugador que ha encontrado un entrenador y se prepara para el combate
            print("¡Has encontrado un entrenador ({})! ¡Prepárate para el combate!".format(trainer_name))
            #Pausa el juego esperando que el jugador presione Enter para continuar
            input("Presiona Enter para continuar...")
            #Anuncia el inicio del combate contra el entrenador encontrado
            print("¡Combate iniciado contra {}!".format(trainer_name))

        #Compara si la posición actual del jugador es específicamente la del primer entrenador definido
        if tuple(my_position) == (4, 6):
            #Mensaje específico para cuando el jugador encuentra al entrenador en la posición (4, 6)
            print("¡Este es el entrenador en la posición (4, 6)!")

            #Inicia variables de vida para un posible sistema de combate
            vida_pikachu = 90  # Vida inicial de Pikachu
            vida_squirtle = 90  # Vida inicial de Squirtle

            #Mientras la vida de ambos sea mayor a 0 se seguirá ejecutando
            while vida_pikachu > 0 and vida_squirtle > 0:
                #Turnos de combate
                print("Turno Squirtle")
                #Squirtle elige aleatoriamente entre dos ataques
                ataque_squirtle = random.randint(1, 2)  
                if ataque_squirtle == 1:
                    print("Squirtle ataca con Placaje")
                    #Reduce la vida de Pikachu
                    vida_pikachu -= 10  
                else:
                    print("Squirtle ataca con Pistola de Agua")
                    #Reduce la vida de Pikachu de forma más severa
                    vida_pikachu -= 11  

                #Muestra las barras de vida de ambos personajes usando el símbolo '#'
                print("La vida de Squirtle es: {}, la vida de Pikachu es: {}".format("#" * vida_squirtle, "#" * vida_pikachu))
                
                #Espera a que se presione cualquier tecla
                msvcrt.getch()

                #Limpiar la pantalla para la próxima ronda
                os.system("cls")

                #Turno de Pikachu
                print("Turno Pikachu")
                print("Selecciona tu ataque:")
                print("1. Bola Voltio")
                print("2. Onda Tueno")
                
                while True:
                    #Espera entrada del jugador
                    choice = msvcrt.getch().decode()  
                    if choice in ["1", "2"]:
                        if choice == "1":
                            #Daño por Bola Voltio
                            vida_squirtle -= 10  
                            print("Pikachu ataca con Bola Voltio")
                        elif choice == "2":
                            #Daño por Onda Tueno
                            vida_squirtle -= 12  
                            print("Pikachu ataca con Onda Tueno")
                        break
                    else:
                        #Mensaje de error si la opción no es válida
                        print("Opción no válida. Por favor, selecciona un número del 1 al 2.")  
                
                #Muestra las barras de vida después del turno de Pikachu
                print("La vida de Squirtle es: {}, la vida de Pikachu es: {}".format("#" * vida_squirtle, "#" * vida_pikachu))
                
                #Espera a que se presione cualquier tecla
                msvcrt.getch()

                #Limpiar la pantalla para la próxima ronda
                os.system("cls")

            #Determinar el resultado del combate
            if vida_squirtle > vida_pikachu:
                print("¡Squirtle gana!")
                #Marca el juego como terminado si Squirtle gana
                game_over = True  
            else:
                print("Has ganado ")

            #Si el juego termina, muestra mensaje de Game Over y termina el juego
            if game_over:
                print("Game Over: Pikachu ha sido derrotado.")
                break  # Termina el bucle principal y finaliza el juego