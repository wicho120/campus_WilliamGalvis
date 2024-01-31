import random

#ejercicio 1

numIngresado = eval(input("Por favor ingrese un numero para validar si es positivo, negativo o cero: "))

if numIngresado < 0:
    print("El numero ingresado es un numero negativo")
elif numIngresado > 0:
    print("El numero ingresado es un numero positivo")
else:
    print("El numero ingresado es un 0")

#ejercicio 2
    
palabraTest = input("Por favor ingrese una palabra para saber si es corta, media o larga: ")

if len(palabraTest) < 5:
    print("La palabra ingresada es corta")
elif len(palabraTest) < 11:
    print("La palabra ingresada es media")
else:
    print("La palabra ingresada es larga")

#ejercicio 3
    
palabraPalin = input("Por favor ingrese una palabra para verificar si es palindromo o no: ")

if palabraPalin == palabraPalin[::-1]:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")

#ejercicio 4 
    
palabraEvaluar = input("Por favor ingrese un texto para ver el numero de vocales y consonantes: ")
contVocales = 0
contConsonantes = 0

for i in palabraEvaluar:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        contVocales += 1
    elif i != " ":
        contConsonantes += 1 

print("El texto ingresado tiene ", contConsonantes, " consonantes y tiene ", contVocales, " vocales")


#ejercicio 5

edadPerro = int(input("Por favor ingrese la edad de su perro: "))

print("La edad de su perro en años de humano es ", (((edadPerro-1)*4)+6))

#ejercicio 6 

print("Bienvenido al juego del dado\n")

while True:
    numDado = random.randint(1,6)
    
    if numDado == 6:
        print("Felicitaciones el dado cayó en el 6")
        break
    else:
        print("El numero que cayó fue ", numDado)

#ejercicio 7
        
print("Vamos a jugar a piedra papel o tijera")

opciones = ["Piedra", "Papel", "tijera"]


tiroMaquina = random.randint(0, 2)

tiroUsuario = int(input("Por favor ingrese su eleccion \n1. Piedra\n2. Papel\n3. Tijera\n"))

if tiroUsuario == tiroMaquina:
    print("Maquina: ", opciones[tiroMaquina], " Usuario: ", opciones[tiroUsuario-1], "\nFue un empate")
elif tiroUsuario == 1 and tiroMaquina == 2:
    print("Maquina: ", opciones[tiroMaquina], " Usuario: ", opciones[tiroUsuario-1], "\nGano la maquina")
elif tiroUsuario == 1 and tiroMaquina == 3:
    print("Maquina: ", opciones[tiroMaquina], " Usuario: ", opciones[tiroUsuario-1], "\nGano el usuario")
elif tiroUsuario == 2 and tiroMaquina == 1:
    print("Maquina: ", opciones[tiroMaquina], " Usuario: ", opciones[tiroUsuario-1], "\nGano el usuario")
elif tiroUsuario == 2 and tiroMaquina == 3:
    print("Maquina: ", opciones[tiroMaquina], " Usuario: ", opciones[tiroUsuario-1], "\nGano la maquina")
elif tiroUsuario == 3 and tiroMaquina == 1:
    print("Maquina: ", opciones[tiroMaquina], " Usuario: ", opciones[tiroUsuario-1], "\nGano la maquina")
elif tiroUsuario == 3 and tiroMaquina == 2:
    print("Maquina: ", opciones[tiroMaquina], " Usuario: ", opciones[tiroUsuario-1], "\nGano el usuario")


#ejercicio 8

numStop = int(input("Por favor ingrese la cantidad de numeros de fibonacci que quiere ver: "))

numFibonacci1 = 0
numFibonacci2 = 0
numFibonacci3 = 1

print(numFibonacci2)
print(numFibonacci3)

for i in range(numStop-2):
    numFibonacci1 = numFibonacci2 + numFibonacci3
    print(numFibonacci1)
    numFibonacci2 = numFibonacci3
    numFibonacci3 = numFibonacci1
