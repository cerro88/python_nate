#6.-Escribir un programa que lea un entero positivo, 
#introducido por el usuario y después muestre en
#pantalla la suma de todos los enteros desde 1 hasta n

n = int(input("Introduzca un número positivo mayor a uno: "))
suma = ((n*(n+1))/2)

print(suma)

#7.-Escribir un programa que pida al usuario su peso 
#(en kg) y estatura (en metros), calcule el índice de
#masa corporal y lo almacene en una variable, 
#y muestre por pantalla la frase Tu índice de 
#masa corporal es <imc> donde <imc> es el índice de 
#masa corporal calculado redondeado con dos decimales.

#El cálculo es relativamente simple: consiste
# en dividir el peso, expresado en kilos, entre
#la estatura, en metros, elevada al cuadrado (kg/m2)

kg = float(input("Introduzca su peso en kilogramos: "))
m = float(input("Introduzca su estatura en metros: "))
imc = round(kg/m**2)

print(imc)

#Escribir un programa que pida al usuario dos números 
#enteros y muestre por pantalla la <n> entre <m> da un 
#cociente <c> y un resto <r> donde <n> y <m> son los 
#números introducidos por el usuario, y <c> y <r> son 
#el cociente y el resto de la división entera 
#respectivamente. 

n = int(input("Introduce un dividendo: "))
m = int(input("Introduce un divisor: "))

cociente = n/m
resto = n%m

print("El cociente de su división es {} y {} su resto".format(cociente,resto))