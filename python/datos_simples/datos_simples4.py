#9.-Escribir un programa que pregunte al usuario una 
#cantidad a invertir, el interés anual y el número de 
#años, y muestre por pantalla el capital obtenido en la 
#inversión.

inversion = float(input("Capital invertido: "))
interes_anual = float(input("Interés anual: "))
años = float(input("Años de inversión: "))

interes = interes_anual / 100
monto_final = inversion * (1 + interes) ** años
ganancia= monto_final - inversion
print(round(ganancia))