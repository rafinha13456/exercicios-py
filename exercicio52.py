n = int(input("Digite um número inteiro: "))
print("Números primos entre 1 e", n, ":")
cont_divisoes = 0
for i in range(2, n + 1):
    eh_primo = True
    for j in range(2, int(i ** 0.5) + 1):
        cont_divisoes += 1
        if i % j == 0:
            eh_primo = False
            break
    if eh_primo:
        print(i)
print("Número de divisões:", cont_divisoes)