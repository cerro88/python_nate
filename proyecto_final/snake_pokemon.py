#¡FINAL BOSS!
#
#El objetivo de este ejercicio final es crear un desafío Pokémon (o lo que más os guste/motive). 
#Cada uno de los objetos será un entrenador pokémon, cuando nos situamos encima de una casilla que contiene un objeto, 
#se lanzará un combate pokémon para luchar contra el entrenador rival. Tenemos que ganar el combate para que el entrenador 
#desaparezca de nuestra lista e ir sucesivamente ganando a cada entrenador (objeto). Cuando hayamos vencido, se terminará el juego.
#
#Nuestro pokémon será Pikachu y cada entrenador tendrá un solo pokémon a libre elección y con los ataques que queráis.



import readchar
import os
import random
#funciones que permiten manejar la entrada y salida en Windows
import msvcrt

POST_X = 0
POST_Y = 1

MAP_WIDTH = 30
MAP_HEIGHT = 30

my_position = [3, 3]

end_game = False
game_over = False


#diccionario de trainers
trainers = {
    (4, 6): "entrenador_1",  
    (5, 27): "entrenador_2",
    (10, 16): "entrenador_3",
    (20, 14): "entrenador_4"
}

#Lista para almacenar las coordenadas de los entrenadores visitados
visited_trainers = []

while not end_game and not game_over:

    while True:

        # Dibujar el mapa
        # Dibuja la parte superior
        print("+" + "-" * MAP_WIDTH * 3 + "+")
        # Este bucle dibuja la parte izquierda del tablero
        for coordinate_y in range(MAP_HEIGHT):
            print("|", end="")

            for coordinate_x in range(MAP_WIDTH):

                draw = " "
                trainer_in_cell = None

                # Verificar si hay un entrenador en esta celda
                for trainer in trainers:
                    if trainer[POST_X] == coordinate_x and trainer[POST_Y] == coordinate_y:
                        if trainer in visited_trainers:
                            # Indica que el entrenador ya ha sido visitado
                            draw = "V"  
                        else:
                            draw = "*"
                            #si el entrenador no ha sido visitado se asigna a esa celda
                            trainer_in_cell = trainer

                            


                # Verificar si la posición actual es la posición del jugador
                if my_position[POST_X] == coordinate_x and my_position[POST_Y] == coordinate_y:
                    draw = "&"

                    if trainer_in_cell and trainer_in_cell not in visited_trainers:
                        # Agregar el entrenador a la lista de visitados
                        visited_trainers.append(trainer_in_cell)  

                print(" {} ".format(draw), end="")
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

        if tuple(my_position) in trainers:
            trainer_name = trainers[tuple(my_position)]
            print("¡Has encontrado un entrenador ({})! ¡Prepárate para el combate!".format(trainer_name))
            input("Presiona Enter para continuar...")
            print("¡Combate iniciado contra {}!".format(trainer_name))

        if tuple(my_position) == (4, 6):
            # Lógica del combate para el entrenador en la posición (4, 6)
            print("¡Este es el entrenador en la posición (4, 6)!")
            # Se inicia una puntuación inicial
            vida_pikachu = 80
            vida_squirtle = 90

            # Mientras la vida de ambos sea mayor a 0 se seguirá ejecutando
            while vida_pikachu > 0 and vida_squirtle > 0:
                # Turnos de combate
                print("Turno pikachu")
                ataque_pikachu = random.randint(1, 2)
                if ataque_pikachu == 1:
                    print("Pikachu ataca con Bola Voltio")
                    vida_squirtle -= 10
                else:
                    print("Pikachu ataca con Onda Tueno")
                    vida_squirtle -= 11
                print("La vida de Pikachu es: {}, la vida de Squirtle es: {}".format("#" * vida_pikachu, "#" * vida_squirtle))
                
                # Espera a que se presione cualquier tecla 
                msvcrt.getch()
                # Limpiar la pantalla
                os.system("cls" if os.name == "nt" else "clear")  
                
                print("Turno squirtle")
                print("Selecciona tu ataque:")
                print("1. Placaje")
                print("2. Pistola de Agua")
                print("3. Burbuja")
                
                ataque_squirtle = random.choice(["P", "A", "B"])
                while True:
                    choice = msvcrt.getch().decode()
                    if choice in ["1", "2", "3"]:
                        if choice == "1":
                            vida_pikachu -= 10
                            print("Squirtle ataca con Placaje")
                        elif choice == "2":
                            vida_pikachu -= 12
                            print("Squirtle ataca con Pistola de Agua")
                        elif choice == "3":
                            vida_pikachu -= 9
                            print("Squirtle ataca con Burbuja")
                        break
                    else:
                        print("Opción no válida. Por favor, selecciona un número del 1 al 3.")
                
                print("La vida de Pikachu es: {}, la vida de Squirtle es: {}".format("#" * vida_pikachu, "#" * vida_squirtle))
                
                # Espera a que se presione cualquier tecla
                msvcrt.getch()

                # Limpiar la pantalla
                os.system("cls" if os.name == "nt" else "clear")  # Limpiar la pantalla

            # Determinar el resultado del combate
            if vida_pikachu > vida_squirtle:
                game_over = True
            else:
                print("¡Squirtle gana!")
        if game_over:
            print("Game Over: Squirtle ha sido derrotado.")
            #rompe el bucle principal y termina el juego
            break  
                

        elif tuple(my_position) == (8, 3):
            # Lógica del combate para el entrenador en la posición (8, 3)
            print("¡Este es el entrenador en la posición (8, 3)!")
            # Se inicia una puntuación inicial
            vida_Blastoise = 80
            vida_squirtle = 90

            # Mientras la vida de ambos sea mayor a 0 se seguirá ejecutando
            while vida_Blastoise > 0 and vida_squirtle > 0:
                # Turnos de combate
                print("Turno Blastoise")
                ataque_Blastoise = random.randint(1, 2)
                if ataque_Blastoise == 1:
                    print("Blastoise ataca con Agua cola")
                    vida_squirtle -= 15
                else:
                    print("Blastoise ataca con Placaje")
                    vida_squirtle -= 9
                print("La vida de Blastoise es: {}, la vida de Squirtle es: {}".format("#" * vida_Blastoise, "#" * vida_squirtle))
                
                # Espera a que se presione cualquier tecla
                msvcrt.getch()
                # Limpiar la pantalla
                os.system("cls")  
                
                print("Turno squirtle")
                print("Selecciona tu ataque:")
                print("1. Placaje")
                print("2. Pistola de Agua")
                print("3. Burbuja")
                
                ataque_squirtle = random.choice(["P", "A", "B"])
                while True:
                    choice = msvcrt.getch().decode()
                    if choice in ["1", "2", "3"]:
                        if choice == "1":
                            vida_Blastoise -= 10
                            print("Squirtle ataca con Placaje")
                        elif choice == "2":
                            vida_Blastoise -= 12
                            print("Squirtle ataca con Pistola de Agua")
                        elif choice == "3":
                            vida_Blastoise -= 9
                            print("Squirtle ataca con Burbuja")
                        break
                    else:
                        print("Opción no válida. Por favor, selecciona un número del 1 al 3.")
                
                print("La vida de Blastoise es: {}, la vida de Squirtle es: {}".format("#" * vida_Blastoise, "#" * vida_squirtle))
                
                # Espera a que se presione cualquier tecla
                msvcrt.getch()

                # Limpiar la pantalla
                os.system("cls" if os.name == "nt" else "clear")  

            # Determinar el resultado del combate
            if vida_Blastoise > vida_squirtle:
                game_over = True
            else:
                print("¡Squirtle gana!")
        if game_over:
            print("Game Over: Squirtle ha sido derrotado.")
            #rompe el bucle principal y termina el juego
            break  

        elif tuple(my_position) == (10, 16):
            # Lógica del combate para el entrenador en la posición (8, 3)
            print("¡Este es el entrenador en la posición (8, 3)!")
            # Se inicia una puntuación inicial
            vida_Charmander = 80
            vida_squirtle = 90

            # Mientras la vida de ambos sea mayor a 0 se seguirá ejecutando
            while vida_Charmander > 0 and vida_squirtle > 0:
                # Turnos de combate
                print("Turno Charmander")
                ataque_Charmander = random.randint(1, 2)
                if ataque_Charmander == 1:
                    print("Charmander ataca con Ascuas")
                    vida_squirtle -= 10
                else:
                    print("Charmander ataca con Garra")
                    vida_squirtle -= 14
                print("La vida de Charmander es: {}, la vida de Squirtle es: {}".format("#" * vida_Charmander, "#" * vida_squirtle))
                
                # Espera a que se presione cualquier tecla
                msvcrt.getch()
                # Limpiar la pantalla
                os.system("cls")  
                
                print("Turno squirtle")
                print("Selecciona tu ataque:")
                print("1. Placaje")
                print("2. Pistola de Agua")
                print("3. Burbuja")
                
                ataque_squirtle = random.choice(["P", "A", "B"])
                while True:
                    choice = msvcrt.getch().decode()
                    if choice in ["1", "2", "3"]:
                        if choice == "1":
                            vida_Charmander -= 10
                            print("Squirtle ataca con Placaje")
                        elif choice == "2":
                            vida_Charmander -= 12
                            print("Squirtle ataca con Pistola de Agua")
                        elif choice == "3":
                            vida_Charmander -= 9
                            print("Squirtle ataca con Burbuja")
                        break
                    else:
                        print("Opción no válida. Por favor, selecciona un número del 1 al 3.")
                
                print("La vida de Charmander es: {}, la vida de Squirtle es: {}".format("#" * vida_Charmander, "#" * vida_squirtle))
                
                # Espera a que se presione cualquier tecla
                msvcrt.getch()

                # Limpiar la pantalla
                os.system("cls" if os.name == "nt" else "clear")  

            # Determinar el resultado del combate
            if vida_Charmander > vida_squirtle:
                game_over = True
            else:
                print("¡Squirtle gana!")

        if game_over:
            print("Game Over: Squirtle ha sido derrotado.")
            break  

        elif tuple(my_position) == (20, 14):
            # Lógica del combate para el entrenador en la posición (8, 3)
            print("¡Este es el entrenador en la posición (8, 3)!")
            # Se inicia una puntuación inicial
            vida_Bulbasaur = 80
            vida_squirtle = 90

            # Mientras la vida de ambos sea mayor a 0 se seguirá ejecutando
            while vida_Bulbasaur > 0 and vida_squirtle > 0:
                # Turnos de combate
                print("Turno Bulbasaur")
                ataque_Bulbasaur = random.randint(1, 2)
                if ataque_Bulbasaur == 1:
                    print("Bulbasaur ataca con Hoja afilada")
                    vida_squirtle -= 10
                else:
                    print("Bulbasaur ataca con Drenadoras")
                    vida_squirtle -= 16
                print("La vida de Bulbasaur es: {}, la vida de Squirtle es: {}".format("#" * vida_Bulbasaur, "#" * vida_squirtle))
                
                # Espera a que se presione cualquier tecla
                msvcrt.getch()
                # Limpiar la pantalla
                os.system("cls")  
                
                print("Turno squirtle")
                print("Selecciona tu ataque:")
                print("1. Placaje")
                print("2. Pistola de Agua")
                print("3. Burbuja")
                
                ataque_squirtle = random.choice(["P", "A", "B"])
                while True:
                    choice = msvcrt.getch().decode()
                    if choice in ["1", "2", "3"]:
                        if choice == "1":
                            vida_Bulbasaur -= 10
                            print("Squirtle ataca con Placaje")
                        elif choice == "2":
                            vida_Bulbasaur -= 12
                            print("Squirtle ataca con Pistola de Agua")
                        elif choice == "3":
                            vida_Bulbasaur -= 9
                            print("Squirtle ataca con Burbuja")
                        break
                    else:
                        print("Opción no válida. Por favor, selecciona un número del 1 al 3.")
                
                print("La vida de Bulbasaur es: {}, la vida de Squirtle es: {}".format("#" * vida_Bulbasaur, "#" * vida_squirtle))
                
                # Espera a que se presione cualquier tecla
                msvcrt.getch()

                # Limpiar la pantalla
                os.system("cls")  

            # Determinar el resultado del combate
            if vida_Bulbasaur > vida_squirtle:
               game_over = True

            else:
                print("¡Squirtle gana!")

        if game_over:
            print("Game Over: Squirtle ha sido derrotado.")
            break  

