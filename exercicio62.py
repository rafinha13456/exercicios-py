nomes_alunos = []
while True:
    nome = input("Digite o nome do aluno (ou 'fim' para terminar): ")
    if nome.lower() == 'fim':
        break
    nomes_alunos.append(nome)
print("Nomes dos alunos do 2DS:", nomes_alunos)