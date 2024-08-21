def potencia(base, expoente):
  """
  Calcula a potência de um número.

  Args:
    base: O número base.
    expoente: O expoente.

  Returns:
    O resultado da potência.
  """
  if expoente <= 10:
    resultado = base ** expoente
    return resultado
  else:
    return "O expoente deve ser no máximo 10."

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

if base > 0 and expoente > 0:
  resultado = potencia(base, expoente)
  print(f"{base} elevado a {expoente} é igual a {resultado}")
else:
  print("Os números devem ser maiores que zero.")