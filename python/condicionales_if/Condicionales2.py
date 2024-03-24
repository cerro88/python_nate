#2.-Escribir un programa que almacene la cadena de caracteres 
#contraseña en una variable, pregunte al usuario por la 
#contraseña e imprima por pantalla si la contraseña introducida
#por el usuario coincide con la guardada en la variable sin 
#tener en cuenta mayúsculas y minúsculas.

contraseña = "pony1234"
contraseña_usuario = input("Introduzca la contraseña: ")
if contraseña != contraseña_usuario.lower():
    print("Contraseña incorrecta.")
else:
    print("Loging OK")