#6.-Escribir un programa que pida al usuario que introduzca
#una frase en la consola y una vocal, y después muestre 
#por pantalla la misma frase pero con la vocal introducida
# en mayúscula.


frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))


#7.-Escribir un programa que pregunte el correo 
#electrónico del usuario en la consola y muestre por 
#pantalla otro correo electrónico con el mismo nombre 
#(la parte delante de la arroba @) pero con dominio ceu.es.

email_usuario = input("Introduzca su email: ")
nuevo_dominio = "ceu.es"
partes_email = email_usuario.split("@")
nuevo_email = partes_email[0] + "@" + nuevo_dominio

print(nuevo_email)


#corrección
email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')


#8.-Escribir un programa que pregunte por consola el precio
# de un producto en euros con dos decimales y muestre por 
#pantalla el número de euros y el número de céntimos del 
#precio introducido.



