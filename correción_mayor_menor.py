
input_usuario = input("Introduzca una lista de números separados por una coma: ")
lista_usuario = [int(numero) for numero in input_usuario.split(",")]


max_num = lista_usuario[0]
min_num = lista_usuario[0]

for n in lista_usuario[1:]:
    if min_num < n:
        min_num = n
    if max_num > n:
        max_num = n

print("El número más grande es: {} y el más pequeño es {}".format(max_num,min_num))
