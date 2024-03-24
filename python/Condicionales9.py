#9
edad = int(input("Introduzca la edad: "))

if(edad < 4):
    print("La entrada es gratis!")
elif((edad >= 4) and (edad <= 18)):
    print("El precio de su entrada es de 5€")
elif(edad > 18):
    print("El precio de su entrada es de 10€")


#corrección
edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")