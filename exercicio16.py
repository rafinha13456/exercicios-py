salario = float(input("Digite o salário do funcionário: "))
percentual_aumento = float(input("Digite o percentual de aumento: "))

valor_aumento = salario * (percentual_aumento / 100)
novo_salario = salario + valor_aumento

print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")