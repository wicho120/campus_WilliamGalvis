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
    
    