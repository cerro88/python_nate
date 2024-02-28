


# se declara una array vacía donde se almacenarán los números que introduzca el usuario
numeros = []
#Se le pide un número al usuario para introducir en la lista
numero_usuario = int(input("Introduce un número en la lista: "))
#se añade ese número a la array vacía
numeros.append(numero_usuario)
#mientras la respuesta del input sea S vuelve a preguntar y almacena el número en la array
while input("¿Deseas introducir más números? (S/n)") == "S":
    #Se le pide un número al usuario para introducir en la lista
    numero_usuario = int(input("Introduce un número en la lista: "))
    #se añade ese número a la array vacía
    numeros.append(numero_usuario)
#Si eso no se cumple imprime la array
print(numeros)







    