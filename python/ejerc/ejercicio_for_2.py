#Cuenta las mayúsculas que hay en una frase

#frase = input("Introduce una frase: ")

#mayusculas = 0

#for letra in frase:
 #   if letra.isupper() == True:
  #      mayusculas +=1
#print("Hay un total de {}".format(mayusculas))


#o

import string
frase = input("Introduce una frase: ")
mayusculas = 0
for letra in frase:
    if letra in frase:
        if letra in string.ascii_uppercase:
            mayusculas += 1

print("Hay un total de {}".format(mayusculas))