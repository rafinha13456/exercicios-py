deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))

rendimento = deposito * (taxa_juros / 100)
total = deposito + rendimento

print(f"Rendimento: R$ {rendimento:.2f}")
print(f"Valor total: R$ {total:.2f}")