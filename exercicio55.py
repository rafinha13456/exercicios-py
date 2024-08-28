frase = input("Digite uma frase: ").upper().replace(" ", "")
frase_invertida = frase[::-1]
if frase == frase_invertida:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")