# Pedir al usuario que introduzca un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Usar un bucle para iterar desde 1 hasta el número proporcionado
for i in range(1, numero + 1):
    # Verificar si el número actual es impar
    if i % 2 != 0:
        # Imprimir el número impar, seguido de una coma, excepto para el último número
        print(i, end=", ")


#corrección
n = int(input("Introduce un número entero positivo: "))
#de esta manera empieza por el uno, hasta número más uno 
# y incrementa en dos , por lo tando solo sacara números impares
# 1 + 2 = 3, 3+2 = 5...etc
for i in range(1, n+1, 2):
    print(i, end=", ")