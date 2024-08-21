soma = 0
for i in range(5):
  numero = int(input(f"Digite o {i+1}º número: "))
  soma += numero
media = soma / 5
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")