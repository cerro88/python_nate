#Una panadería vende barras de pan a 3.49€ cada una. 
#El pan que no es el día tiene un descuento del 60%. 
#Escribir un programa que comience leyendo el número de 
#barras vendidas que no son del día. Después el 
#programa debe mostrar el precio habitual de una barra 
#de pan, el descuento que se le hace por no ser fresca 
#y el coste final total.

pan_dia = 3.49
descuento = 0.6
pan_dia_ant = 3.49 * (1-0.6)
barras = int(input("Barras vendidas del dia anterior:"))

total = float(barras * pan_dia_ant)

print("El precio de una barra de pan es", + pan_dia,)
print("Al ser del día anterior se le aplica un descuentos del", + descuento * 100, "%")
print("El precio total de las barras es", round(total,2), "€")