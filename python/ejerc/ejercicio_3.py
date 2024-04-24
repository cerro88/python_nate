#Tabla de multiplicar
#solo mostrará los múltiplos 
a = int(input("Número a multiplicar: "))
#se define el multiplo
multiplo = 2

for n in range (1,11):
   if n % 2 == 0:
    print("{} * {} = {}".format(n, a, n * a))

