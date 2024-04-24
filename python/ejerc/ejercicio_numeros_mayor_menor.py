#comentar


input_usuario = input("Introduzca una lista de números separados por una coma: ")
lista_usuario = input_usuario.split(",")
numeros_limpios =[]

for numero in lista_usuario:
    numeros_limpios.append(int(numero))

print(numeros_limpios)

max_num = numeros_limpios[0]
min_num = numeros_limpios[0]

for n in numeros_limpios:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print("El número más grande es: {} y el más pequeño es {}".format(max_num,min_num))
