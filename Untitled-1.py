# Dicionário com os valores das passagens
passagens = {
    "Urca": 4.50,
    "Olaria": 5.00,
    "Copacabana": 9.00
}

# Variável de controle
continuar = True

# Laço que continua enquanto a variável "continuar" for True
while continuar:
    # Pergunta ao usuário o destino
    destino = input("Para qual destino deseja viajar? (Urca, Olaria, Copacabana) ou digite 'sair' para encerrar: ")

    # Verifica se o usuário quer sair
    if destino.lower() == 'sair':
        print("Encerrando o programa.")
        continuar = False  # Define a variável para parar o loop

    # Verifica se o destino está no dicionário e exibe o valor da passagem
    elif destino in passagens:
        print(f"O valor da passagem para {destino} é R$ {passagens[destino]:.2f}.")
    else:
        print("Destino não encontrado. Tente novamente.")