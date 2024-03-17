#Escribir un programa que pregunte por consola por los 
#productos de una cesta de la compra, separados por comas, 
#y muestre por
#pantalla cada uno de los productos en una línea distinta.

lista = input("Introduce los productos de tu cesta de la compra: ")
print(lista.replace(",", "\n"))

#o print('\n'.join(cesta.split(',')))