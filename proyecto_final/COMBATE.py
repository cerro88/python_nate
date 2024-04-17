import os
import random
import msvcrt

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
    os.system("cls" if os.name == "nt" else "clear")  # Limpiar la pantalla

# Determinar el resultado del combate
if vida_Bulbasaur > vida_squirtle:
    print("¡Bulbasaur gana!")
else:
    print("¡Squirtle gana!")