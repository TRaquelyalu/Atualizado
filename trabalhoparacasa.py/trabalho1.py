'''
1.	Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

'''

def pedir_nota():
    while True:
        try:
            nota = float(input("Informe uma nota entre 0 e 10: "))
            if 0 <= nota <= 10:
                print(f"Nota válida: {nota}")
                break
            else:
                print("Valor inválido! A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

pedir_nota()
