'''
7.	Faça um programa que leia 5 números e informe o maior número.
'''

def encontrar_maior():
    maior = None  # Variável para armazenar o maior número
    for i in range(5):
        numero = float(input(f"Informe o {i+1}º número: "))  # Solicita o número ao usuário
        if maior is None or numero > maior:
            maior = numero  # Atualiza o maior número se o atual for maior
    print(f"O maior número informado foi: {maior}")

# Chamada da função principal
encontrar_maior()