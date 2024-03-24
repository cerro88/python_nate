#Tabla de multiplicar
#solo mostrará los múltiplos 
a = int(input("Número a multiplicar: "))
#se define el multiplo
multiplo = 2
#para n en el rango del 1-10
for n in range (1,11):
    #if n % 2 == 0: #si se hace así solo multiplica por los múltiplos de dos
   #se define el resultado 
   resultado = (n * a)
   #si el resultado da como resto 0 al dividirlo por 2
   if resultado % multiplo == 0:
    #imprime n * a = x 
    print("{} * {} = {}".format(n, a, resultado))

