palavra = input("Digite uma palavra: ")
consoantes = []
for letra in palavra:
    if letra.lower() in "bcdfghjklmnpqrstvwxyz":
        consoantes.append(letra)
print("Consoantes:", consoantes)