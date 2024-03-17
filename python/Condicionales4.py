#Escribir un programa que pida al usuario un número entero y 
#muestre por pantalla si es par o impar.

n = int(input("Introduzca un número: "))
comprovacion = n % 2 
if comprovacion == 0:
    print(str(n) + " es un número par")
else:
    print(str(n) + " es un número impar")