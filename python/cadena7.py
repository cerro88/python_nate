#8.-Escribir un programa que pregunte por consola el precio
# de un producto en euros con dos decimales y muestre por 
#pantalla el número de euros y el número de céntimos del 
#precio introducido.

precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

#9.-Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato 
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior
#para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

nacimiento = input("Introduce tu fecha de nacimiento dd/mm/aaaa:  ")
print ("Dia", nacimiento[:2])
print ("Mes", nacimiento[3:5])
print ("Año", nacimiento[6:])

#Adaptar el programa anterior para que también funcione cuando 
#el día o el mes se introduzcan con un solo carácter.
fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)