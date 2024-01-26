
print("Estamos vendiendo un producto al por mayor a 10 dolares por docena")
numProductos = int(input("cuantos productos quiere comprar: "))

numDocenas = numProductos/12

if numDocenas <= 3:
    print("Por su compra su decuento es del 10%") 
    print("su valor a pagar es: ", str((numDocenas * 10)-((numDocenas*10)*0.1)) , " dolares")
elif numDocenas >= 4:
    print("Por su compra su decuento es del 15%")
    print("y su valor a pagar es: " + str((numDocenas * 10)-((numDocenas*10)*0.15)) + " dolares, ademas le regalamos " + str(round(numDocenas-3)) + " productos")

