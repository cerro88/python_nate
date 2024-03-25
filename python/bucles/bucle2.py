#2. Escribir un programa que pregunte al usuario la edad
# y enseñe por pantalla los años que ha cumplido desde 1 a su edad

#Se al macena el valor de la edad en la variable age
# COMO INTEGER PORQUE ES NÚMERO
age = int(input("¿Cuál es tu edad?"))

#Mientras la iteración este en el rango de la edad
for i in range(age):
    #se pasa a string el valor integer
    print("Ha cumplido " + str(i+1))
