#Los teléfonos de una empresa tienen el siguiente 
#formato prefijo-número-extension donde el prefijo es el
#código del país +34, y la extensión tiene dos dígitos 
#(por ejemplo +34-913724710-56). 
#Escribir un programa que pregunte por un número de 
#teléfono con este formato y muestre por pantalla el 
#número de teléfono sin el prefijo y la extensión.


tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])
print('El prefijo es', tel[0:3])
print('La extensión marcada es: ', tel[14:16])