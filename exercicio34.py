def calcula_peso_ideal(h, sexo):
  """
  Calcula o peso ideal de uma pessoa.

  Args:
    h: Altura da pessoa em metros.
    sexo: Sexo da pessoa ('H' para homens, 'M' para mulheres).

  Returns:
    O peso ideal da pessoa em kg.
  """
  if sexo == 'H':
    peso_ideal = (72.7 * h) - 58
  elif sexo == 'M':
    peso_ideal = (62.1 * h) - 44.7
  else:
    return "Sexo inválido. Por favor, insira 'H' para homens ou 'M' para mulheres."
  return peso_ideal
