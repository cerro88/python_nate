#Si los números son menores o iguales a 5 multiplica por 15, sin son mayores que 5  y menores que 10 multiplica por 5, si es igual a 10 por 2

valores = range(1,11)

for n in valores:
    if n <= 5:
        resultado = (n * 15)
        print("resultado: {}".format(resultado))
    elif n > 5 and n < 10:
        resultado = (n * 5)
        print("resultado: {}".format(resultado))
    elif n == 10:
        resultado = (n * 2)
        print("resultado: {}".format(resultado))