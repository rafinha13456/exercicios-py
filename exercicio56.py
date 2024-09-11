numero = int(input("Digite um número entre 0 e 99: "))

unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

if numero < 10:
    print(unidades[numero])
elif numero < 20:
    if numero == 10:
        print("dez")
    elif numero == 11:
        print("onze")
    elif numero == 12:
        print("doze")
    elif numero == 13:
        print("treze")
    elif numero == 14:
        print("quatorze")
    elif numero == 15:
        print("quinze")
    elif numero == 16:
        print("dezesseis")
    elif numero == 17:
        print("dezessete")
    elif numero == 18:
        print("dezoito")
    elif numero == 19:
        print("dezenove")
else:
    dezena = numero // 10
    unidade = numero % 10
    if unidade == 0:
        print(dezenas[dezena])
    else:
        print(dezenas[dezena], "e", unidades[unidade])