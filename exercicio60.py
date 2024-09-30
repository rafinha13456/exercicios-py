numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

if fim < inicio:
    print("O valor final deve ser maior que o inicial.")
else:
    print(f"Tabuada de {numero} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")