#7

renta_anual = float(input("Introduzca su renta anual: "))

if renta_anual < 10000:
    print("El tipo impositivo de su renta anual es del 5%")
if renta_anual >= 10000 and renta_anual < 20000:
    print("El tipo impositivo de su renta anual es del 15%")
if renta_anual >= 20000 and renta_anual < 35000:
    print("El tipo impositivo de su renta anual es del 20%")
if renta_anual >= 35000 and renta_anual < 60000:
    print("El tipo impositivo de su renta anual es del 30%")
if renta_anual >= 60000:
    print("El tipo impositivo de su renta anual es del 45%")


#Corrección

# Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')
