#3.-Escribir un programa que pida al usuario dos números 
#y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.

num1 = int(input("Introduzca el dividendo: "))
num2 = int(input("Introduzca el divisor: "))

while num2 == 0:
    print("No se puede dividir por 0")
    num2 = int(input("Introduzca el divisor: "))

print(num1 / num2)


#correción

n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisior: "))
if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)