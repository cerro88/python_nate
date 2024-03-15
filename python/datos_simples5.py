#Una juguetería tiene mucho éxito en dos de sus 
#productos: payasos y muñecas. Suele hacer venta por 
#correo y la empresa de logística les cobra por peso de 
#cada paquete así que deben calcular el peso de los 
#payasos y muñecas que saldrán en cada paquete a demanda. #
#Cada payaso pesa 112 g y cada muñeca 75 g. 
#Escribir un programa que lea el número de payasos y 
#muñecas vendidos en el último pedido y calcule el peso total
#del paquete

payasos = 112
muñeca = 75
payasos_vendidos = int(input("Total de payasos vendidos: "))
muñecas_vendidas = int(input("Total de muñecas vendidas: "))
peso_payasos = payasos_vendidos * payasos / 1000
peso_muñecas = muñecas_vendidas * muñeca / 1000
peso_total = print(peso_muñecas + peso_payasos, "KG")
