edad = int(input("Por favor ingrese su edad para ver si es apto para votar: "))

if edad >= 18:
    print("Felicitaciones usted puede votar")
else:
    print("Usted no puede botar")


calificacion = int(input("Por favor ingrese una calificacion de 1 a 100: "))

if calificacion <= 25:
    print("Su calificacion es D")
elif calificacion <= 50:
    print("Su calificacion es C")
elif calificacion <= 75:
    print("Su calificacion es B")
elif calificacion <= 100:
    print("Su calificacion es A")


tipoComida = input("Por favor ingrese el tipo de comida que mas le gusta: ")

if tipoComida == "Comida china":
    print("Le recomendamos el restaurante yakuza bga")
elif tipoComida == "Comida italiana":
    print("Le recomendamos el restaurante dominos pizza")
elif tipoComida == "Comida tipica":
    print("Le recomendamos el restaurante la mazorca")



contraUsuario = input("Por favor ingrese su contraseñ: ")
contraUsuarioCorrecta = "hola"

if contraUsuario == contraUsuarioCorrecta:
    print("felicitaciones entraste a la app")
else:
    print("Contraseña incorrecta")



palabraTest = input("Por favor ingrese una palabra para verificar si es palindromo o no: ")

if palabraTest == palabraTest[::-1]:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")