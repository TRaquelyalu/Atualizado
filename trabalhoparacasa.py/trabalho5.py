'''
5.	Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

def validar_entrada(mensagem, tipo=float):
    # Função para validar a entrada do usuário (valores positivos e numéricos)
    while True:
        try:
            valor = tipo(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Erro: O valor deve ser maior que zero.")
        except ValueError:
            print("Erro: Insira um número válido.")

def calcular_crescimento():
    while True:
        # Entrada das populações e validação
        populacao_a = validar_entrada("Informe a população inicial do país A: ", int)
        populacao_b = validar_entrada("Informe a população inicial do país B: ", int)
        taxa_a = validar_entrada("Informe a taxa de crescimento anual do país A (%): ")
        taxa_b = validar_entrada("Informe a taxa de crescimento anual do país B (%): ")

        anos = 0

        # Cálculo dos anos até que a população de A ultrapasse ou iguale a de B
        while populacao_a < populacao_b:
            populacao_a += populacao_a * (taxa_a / 100)
            populacao_b += populacao_b * (taxa_b / 100)
            anos += 1

        print(f"Levará {anos} anos para a população do país A ultrapassar ou igualar a população do país B.")

        # Pergunta ao usuário se ele deseja repetir o cálculo
        repetir = input("Deseja realizar outra simulação? (S/N): ").strip().lower()
        if repetir != 's':
            print("Encerrando o programa.")
            break

# Chamada da função principal para iniciar o programa
calcular_crescimento()