def tipo_triangulo(a, b, c):
    if a == b and b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

tipo = tipo_triangulo(lado1, lado2, lado3)

print("O triângulo é", tipo)