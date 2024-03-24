#8
bonoficacion = 2400
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


