#Escribir un programa que pregunte el nombre 
#del usuario en la consola y un número entero e 
#imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = [""]

nombre = input("¿Cuál es tu nombre? "), int(input("Introduce un número mayor que 1: ")) #esta manera no es eficiente y induce a errores

print(nombre)

usuario = nombre[0]
numero = nombre[1] 

for n in range(0,numero):
    print (usuario)


print("Esta es la correción del Ejercicio:")

nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))

#https://aprendeconalf.es/docencia/python/ejercicios/cadenas/