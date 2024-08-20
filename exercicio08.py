letra = input("Digite uma letra: ")

if letra.lower() in "aeiou":
    print("A letra", letra, "é uma vogal.")
else:
    print("A letra", letra, "é uma consoante.")