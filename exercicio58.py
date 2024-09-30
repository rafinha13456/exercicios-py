tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()
litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))

if tipo_combustivel == "A":
    if litros_vendidos <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco_litro = 3.90
elif tipo_combustivel == "G":
    if litros_vendidos <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco_litro = 5.50
else:
    print("Tipo de combustível inválido.")
    exit()

valor_total = (preco_litro * litros_vendidos) * (1 - desconto)
print(f"Valor a ser pago: R$ {valor_total:.2f}")