#Cuenta los espacios, puntos y comas que hay en una frase
#podría ser un imput para que el usuario introduzca la frase
texto_usuario = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin laoreet, leo sit amet fringilla placerat, augue ipsum rutrum diam, quis lobortis lectus orci vel enim."
espacios = 0
comas = 0
puntos = 0

for letra in texto_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ",":
        comas += 1
    elif letra == ".":
        puntos += 1


#print("Espacios {}".format(espacios))
#print("Puntos {}".format(puntos))
#print("Comas {}".format(comas))
print("Espacios: {}, Puntos: {}, Comas: {}".format(espacios, puntos, comas))


