#Programa para hacer la lista de la compra

#Se define un array o lista vacia
lista_compra = []
#Se inicia la variable sin asignar un valor específico
input_del_usuario = None
#informa al usuario del scrip
print("Programa lista de la compra")
#Esto crea un bucle infinito que solo se detendrá si encuentra una instrucción dentro del bucle
while True:
    #Se crea una variable que guardará el imput del usuario
    input_del_usuario = input("¿Qué desea comprar? ([Q] Para salir): ")
    #si el imput es igual a Q se acaba el programa
    if input_del_usuario == "Q" or input_del_usuario == "q":
        break
    #si el input está en la lista de la compra
    elif input_del_usuario in lista_compra:
        #imprime que ese artículo ya está en la lista
        print("{} ya está en lista".format(input_del_usuario))
    #pero si no pregunta si se quiere añadir ese artículo a la lista
    else:
        if input("¿Quieres añadir {} a la lista?".format(input_del_usuario)) == "S":
            #añade a la lista el input del usuario
            lista_compra.append(input_del_usuario)
#se imprime la lista de la compra
print("La lista de la compra es: ")
print(lista_compra)