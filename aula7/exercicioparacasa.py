# Solicita quantos alunos o usuário quer calcular a média
alunos = int(input("Quantos alunos deseja calcular a média (0 para sair): "))

# Laço para processar os alunos
for i in range(alunos):
    nome = input(f"Nome do aluno {i + 1}: ")
    nota1 = float(input("Primeira nota tirada: "))
    nota2 = float(input("Segunda nota tirada: "))
    media = (nota1 + nota2) / 2

    # Determina se o aluno está aprovado ou reprovado
    if media >= 6.5:
        resultado = f"{nome} - Média: {media:.2f} - Aprovado"
    else:
        resultado = f"{nome} - Média: {media:.2f} - Reprovado"

    # Solicita quantas vezes o usuário deseja repetir a exibição do resultado
    repeticoes = int(input("Quantas vezes deseja exibir a informação deste aluno? "))
    
    # Exibe a informação do aluno repetidamente
    for _ in range(repeticoes):
        print(resultado)

print("Processo finalizado.")