#8
bonificacion = 2400
inaceptable = 0.0
Aceptable = 0.4
Meritorio = 0.6 

puntos = float(input("Introduce tu puntuación: "))

if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == Aceptable:
    nivel = "Aceptable"
elif puntos >= Meritorio:
    nivel = "Meritorio"

bonificacion_trabajador = puntos*bonificacion
print("Su nivel es " + str(nivel) + " por lo tanto su bonificación es de: " + str(bonificacion_trabajador) + "€")


#correción
bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))