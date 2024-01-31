def imprmirSaludo(nombre):
    retornar = "Hola " + nombre
    return retornar

def calcularAreaCuadraro(medidaLado):
    areaC = medidaLado ** 2
    str(areaC)
    return areaC


nombreUsuario = input("Por favor ingrese su nombre: ")




medidaLado = int(input("Por favor ingrese la medida de algunos de los lados del cuadrado: "))

print(imprmirSaludo(nombreUsuario), ", El area del cuadrado con las medidas ingresadas es: ", calcularAreaCuadraro(medidaLado))


