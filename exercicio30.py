def calculadora():
    """
    Realiza operações matemáticas básicas.

    Recebe dois números e o tipo de operação desejada pelo usuário e exibe o resultado.
    """

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    operacao = input("Digite a operação desejada (+, -, *, /): ")

    if operacao == "+":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif operacao == "-":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif operacao == "*":
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    elif operacao == "/":
        if num2 == 0:
            print("Erro: Divisão por zero não permitida.")
        else:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
    else:
        print("Operação inválida.")

calculadora()