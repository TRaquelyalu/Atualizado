while True:
    alunos = int(input("Quantos alunos deseja calcular a média (0 para sair): "))
    
    if alunos == 0:
        print("Programa encerrado.")
        break

    for i in range(alunos):
        nome = input(f"Nome do aluno {i + 1}: ")
        nota1 = float(input("Primeira nota tirada: "))
        nota2 = float(input("Segunda nota tirada: "))
        media = (nota1 + nota2) / 2

        if media >= 6.5:
            print(f"{nome} - Média: {media:.2f} - Aprovado")
        else:
            print(f"{nome} - Média: {media:.2f} - Reprovado")

    repetir = input("Deseja calcular a média de mais alunos? (s/n): ")
    if repetir.lower() != 's':
        print("Programa encerrado.")
        break