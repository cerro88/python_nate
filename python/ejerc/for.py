#Se definen las variables vocales y frase

vocales = ["a","e", "i", "o", "u"]
frase = "Hola, estoy aprendiendo python"

#contador a 0 de vocales encontradas 
vocales_encontradas = 0

#por cada letra en la frase
for letra in frase:
    #si la letra está en vocales
    if letra in vocales:
        #imprime la vocal encontrada
        print("He encontrado una '{}'".format(letra))
        #suma 1 a vocales encontradas
        vocales_encontradas += 1

#imprime el texto vovales encontradas: que devuelva el
#valor de la variable vocales encontradas
print("vocales_encontradas: {}".format(vocales_encontradas))