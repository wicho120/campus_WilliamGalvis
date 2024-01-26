horasTrabajadas = int(input("Por favor ingrese la cantidad de horas trabajadas: "))

if horasTrabajadas < 10:
    print("Su pago por hora es: 5 dolares y su pago total es: ", horasTrabajadas*5)
elif horasTrabajadas >= 10 and horasTrabajadas < 20:
    print("Su pago por hora es: 10 dolares y su pago total es: ", horasTrabajadas*10, " dolares")
else:
    print("Su pago por hora es: 5 dolares y su pago total es: ", horasTrabajadas*15, " dolares")14