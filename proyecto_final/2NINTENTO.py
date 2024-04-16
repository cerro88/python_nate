import readchar
import os
import random 
from random import randint


POST_X = 0
POST_Y = 1

my_position = [3, 3]
new_position = [7,7]

trainers = {
    (5, 10): "entrenador1",
    (7, 2): "entrenador2",
}

MAP_WIDTH = 20
MAP_HEIGHT = 20

end_game = False
died = False

visited_trainers = []

while True:
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = " "

           
            # Verifica si el jugador está en la misma posición que un asterisco
            for trainer in trainers:
                if trainer[POST_X] == coordinate_x and trainer[POST_Y] == coordinate_y:
                    char_to_draw = "*"

            # Dibuja al jugador
            if my_position[POST_X] == coordinate_x and my_position[POST_Y] == coordinate_y:
                char_to_draw = "@"

            print(" {} ".format(char_to_draw), end="")
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
        my_position[POST_X] %= MAP_WIDTH
    elif direction == "d":
        my_position[POST_X] += 1
        my_position[POST_X] %= MAP_WIDTH
    elif direction == "q":
        break

    # Si el jugador está en la misma posición que un asterisco, se inicia el combate
    if tuple(my_position) in trainers:
        print("¡Has encontrado un entrenador! ¡Prepárate para el combate!")
        input("Presiona Enter para continuar...")
        print("¡Combate iniciado contra {}!".format(trainers[tuple(my_position)]))
        #lógica del combate
        #se inicia una puntuación inicial 
        vida_pikachu = 80
        vida_squiertle = 90

        # mientras la vida de ambos sea mayor a 0 se seguirá ejecutando

        while vida_pikachu > 0 and vida_squiertle > 0:
            #turnos de combate

            print("Turno pikachu")

            # 
            ataque_pikachu = random.randint(1,2)
            if ataque_pikachu == 1:
                print("Pikachu ataca con Bola Voltio")
                vida_squiertle -= 10
            else:
                print("Pikachu ataca con Onda Tueno")
                vida_squiertle -= 11
            print("La vida de Pikachu es: {}, la vida de squiertle es {}".format("#" * vida_pikachu,"#" * vida_squiertle))

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

            print("La vida de Picachu es: {}, la vida de squiertle es {}".format("#" * vida_pikachu,"#" * vida_squiertle))
            input("Enter para continuar...\n\n")

            if vida_pikachu > vida_squiertle:
                print("Pikachu gana!")
            else:
                print("Squiertle gana!")
    
                

        # Elimina al asterisco temporalmente del tablero
        del trainers[tuple(my_position)]

        # Una vez que el combate termina, el asterisco vuelve al tablero
        trainers[tuple(my_position)] = "entrenador_vencido"

  

    os.system("cls")  