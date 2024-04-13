import readchar
import os
from random import randint

POST_X = 0
POST_Y = 1

MAP_WIDTH = 30
MAP_HEIGHT = 30

my_position = [2, 3]

trainers = {
    (4, 6): "entrenador_1",
    (5, 4): "entrenador_2",
    (10, 16): "entrenador_3",
    (20, 14): "entrenador_4"
}

trainers_to_remove = []

while True:
    os.system("cls")

    # Dibujar el mapa
    # Dibujar el mapa
    # Dibuja la parte superior
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    # Este bucle dibuja la parte izquierda del tablero
    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "

            # Verificar si hay un entrenador en esta celda
            for map_trainer in trainers:
                if map_trainer[POST_X] == coordinate_x and map_trainer[POST_Y] == coordinate_y:
                    char_to_draw = "*"

            # Verificar si la posición actual es la posición del jugador
            if my_position[POST_X] == coordinate_x and my_position[POST_Y] == coordinate_y:
                char_to_draw = "&"


            print(" {} ".format(char_to_draw), end="")
        print("|")

    # Se imprime el borde derecho del tablero
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = readchar.readchar()

    # Movimiento del jugador
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
        break

    # Verificar si el jugador está en una posición con un entrenador
    for trainer_pos, combat_type in trainers.items():
        if my_position[POST_X] == trainer_pos[POST_X] and my_position[POST_Y] == trainer_pos[POST_Y]:
                    if combat_type == "entrenador_1":
                        print("¡Combate contra el entrenador 1!")
                        # Lógica de combate para el entrenador 1
                        # se inicia una puntuación inicial
                        vida_pikachu = 80
                        vida_squiertle = 90

                        # mientras la vida de ambos sea mayor a 0 se seguirá ejecutando
                        while vida_pikachu > 0 and vida_squiertle > 0:
                            # turnos de combate
                            print("Turno pikachu")

                            ataque_pikachu = randint(1, 2)
                            if ataque_pikachu == 1:
                                print("Pikachu ataca con Bola Voltio")
                                vida_squiertle -= 10
                            else:
                                print("Pikachu ataca con Onda Tueno")
                                vida_squiertle -= 11
                            print("La vida de Pikachu es: {}, la vida de squiertle es {}".format("#" * vida_pikachu, "#" * vida_squiertle))

                            input("Enter para continuar...\n\n")

                            print("Turno squiertle")

                            ataque_squiertle = None
                            while ataque_squiertle != "P" and ataque_squiertle != "A" and ataque_squiertle != "B":
                                ataque_squiertle = input("¿Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja: ")

                            if ataque_squiertle == "P":
                                vida_pikachu -= 10
                            elif ataque_squiertle == "A":
                                vida_pikachu -= 12
                            elif ataque_squiertle == "B":
                                vida_pikachu -= 9

                            print("La vida de Pikachu es: {}, la vida de squiertle es {}".format("#" * vida_pikachu, "#" * vida_squiertle))
                            input("Enter para continuar...\n\n")

                            if vida_pikachu > vida_squiertle:
                                print("Pikachu gana!")
                            else:
                                print("Squiertle gana!")

                        # Eliminar el entrenador de la lista después del combate
                        del trainers[trainer_pos]

                        # Eliminar los entrenadores marcados para eliminación
                        for trainer_pos in trainers_to_remove:
                            del trainers[trainer_pos]

                        # Restablecer la posición del jugador después de terminar el combate
                        my_position = [2, 3]

                    elif combat_type == "entrenador_2":
                        print("¡Combate contra el entrenador 2!")
                        # Lógica de combate para el entrenador 2
                        # se inicia una puntuación inicial
                        vida_Charmander = 80
                        vida_squiertle = 90

                        # mientras la vida de ambos sea mayor a 0 se seguirá ejecutando
                        while vida_Charmander > 0 and vida_squiertle > 0:
                            # turnos de combate
                            print("Turno Charmander")

                            ataque_charmander = randint(1, 2)
                            if ataque_charmander == 10:
                                print("Charmander ataca con Arañazo Scratch")
                                vida_squiertle -= 15
                            else:
                                print("Pikachu ataca con Pantalla de humo")
                                vida_squiertle -= 10
                            print("La vida de Charmander es: {}, la vida de squiertle es {}".format("#" * vida_Charmander, "#" * vida_squiertle))

                            input("Enter para continuar...\n\n")

                            print("Turno squiertle")

                            ataque_squiertle = None
                            while ataque_squiertle != "P" and ataque_squiertle != "A" and ataque_squiertle != "B":
                                ataque_squiertle = input("¿Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja: ")

                            if ataque_squiertle == "P":
                                vida_Charmander -= 15
                            elif ataque_squiertle == "A":
                                vida_Charmander -= 12
                            elif ataque_squiertle == "B":
                                vida_Charmander -= 19

                            print("La vida de Charmander es: {}, la vida de squiertle es {}".format("#" * vida_Charmander, "#" * vida_squiertle))
                            input("Enter para continuar...\n\n")

                            if vida_Charmander > vida_squiertle:
                                print("Charmander gana!")
                            else:
                                print("Squiertle gana!")

                        # Eliminar el entrenador de la lista después del combate
                        del trainers[trainer_pos]

                        for trainer_pos in trainers_to_remove:
                            del trainers[trainer_pos]

                    elif combat_type == "entrenador_3":
                        print("¡Combate contra el entrenador 3!")
                        # Lógica de combate para el entrenador 3
                        vida_blastoise = 80
                        vida_squiertle = 90

                        while vida_blastoise > 0 and vida_squiertle > 0:
                            # turnos de combate
                            print("Turno Blastoise")

                            ataque_blastoise = randint(1, 2)
                            if ataque_blastoise == 1:
                                print("Blastoise ataca con Terremoto Earthquake")
                                vida_squiertle -= 18
                            else:
                                print("Blastoise ataca con Hidropulso")
                                vida_squiertle -= 7
                            print("La vida de Blastoise es: {}, la vida de squiertle es {}".format("#" * vida_blastoise, "#" * vida_squiertle))

                            input("Enter para continuar...\n\n")

                            print("Turno squiertle")

                            ataque_squiertle = None
                            while ataque_squiertle != "P" and ataque_squiertle != "A" and ataque_squiertle != "B":
                                ataque_squiertle = input("¿Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja: ")

                            if ataque_squiertle == "P":
                                vida_blastoise -= 15
                            elif ataque_squiertle == "A":
                                vida_blastoise -= 12
                            elif ataque_squiertle == "B":
                                vida_blastoise -= 19

                            print("La vida de Blastoise es: {}, la vida de squiertle es {}".format("#" * vida_blastoise, "#" * vida_squiertle))
                            input("Enter para continuar...\n\n")

                            if vida_blastoise > vida_squiertle:
                                print("Blatoise gana!")
                            else:
                                print("Squiertle gana!")

                        # Eliminar el entrenador de la lista después del combate
                        del trainers[trainer_pos]

                        for trainer_pos in trainers_to_remove:
                            del trainers[trainer_pos]

                    elif combat_type == "entrenador_4":
                        print("¡Combate contra el entrenador 4!")
                        # Lógica de combate para el entrenador 4
                        vida_charizard = 80
                        vida_squirtle = 90

                        while vida_charizard > 0 and vida_squirtle > 0:
                            # Turnos de combate
                            print("Turno Charizard")

                            ataque_charizard = randint(1, 2)
                            if ataque_charizard == 1:
                                print("Charizard ataca con Terremoto Earthquake")
                                vida_squirtle -= 18
                            else:
                                print("Charizard ataca con Llamarada Flamethrower")
                                vida_squirtle -= 7

                            print("La vida de Charizard es: {}, la vida de Squirtle es: {}".format("#" * vida_charizard, "#" * vida_squirtle))
                            input("Enter para continuar...\n\n")

                            print("Turno Squirtle")

                            ataque_squirtle = None
                            while ataque_squirtle not in ["P", "A", "B"]:
                                ataque_squirtle = input("¿Qué ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja: ")

                            if ataque_squirtle == "P":
                                vida_charizard -= 15
                            elif ataque_squirtle == "A":
                                vida_charizard -= 12
                            elif ataque_squirtle == "B":
                                vida_charizard -= 19

                            print("La vida de Charizard es: {}, la vida de Squirtle es: {}".format("#" * vida_charizard, "#" * vida_squirtle))
                            input("Enter para continuar...\n\n")

                            if vida_charizard > vida_squirtle:
                                print("Charizard gana!")
                            else:
                                print("Squirtle gana!")

                        # Eliminar el entrenador de la lista después del combate
                        del trainers[trainer_pos]
                        for trainer_pos in trainers_to_remove:
                            del trainers[trainer_pos]
              