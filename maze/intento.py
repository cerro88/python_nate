
#se define la anchura del tablero
MAP_WIDTH = 20
#se define la altura del tablero
MAP_HEIGHT = 15

#dibuja la parte superior
#dibujará + seguido de tantos guiones como el map_width
#multiplicado por tres lo que define la anchuna --- de casa casilla
#finalizando la esquina con +
print("+" + "-" * MAP_WIDTH * 3 + "+")


#este bucle for recorre el rando de map_height en la coordenada y
#imprimiendo |, end evita el salto de línea
#este bucle dibuja la parte izquierda del tablero
for coordinate_y in range(MAP_HEIGHT):
    print("|", end="")
    #dentro otro bucle que recorrerá el rango de map_widht en la coordenada x 
    #imprimiendo tres espacios
    for coordinate_x in range(MAP_WIDTH):
        print("   ", end="")
    #se imprime el borde derecho del tablero
    print("|")

#dibuja la parte inferior
#dibujará + seguido de tantos guiones como el map_width
#multiplicado por tres lo que define la anchuna --- de casa casilla
#finalizando la esquina con +
print("+" + "-" * MAP_WIDTH * 3 + "+")