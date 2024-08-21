import math

def bhaskara(a, b, c):
  delta = (b**2) - 4*(a*c)
  if delta < 0:
    return "A equação não possui raízes reais."
  else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return f"As raízes da equação são: x1 = {x1:.2f} e x2 = {x2:.2f}"

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
  print("A equação não é do 2º grau.")
else:
  print(bhaskara(a, b, c))