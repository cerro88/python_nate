#!/usr/bin/env python3

from random import randint

#se inicia una puntuación inicial 
vida_pikachu = 80
vida_squiertle = 90

# mientras la vida de ambos sea mayor a 0 se seguirá ejecutando

while vida_pikachu > 0 and vida_squiertle > 0:
    #turnos de combate

    print("Turno pikachu")

    # 
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltio")
        vida_squiertle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
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
