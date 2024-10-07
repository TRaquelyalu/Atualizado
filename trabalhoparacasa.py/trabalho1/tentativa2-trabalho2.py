'''
2.	Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações
'''
def pedir_credenciais():
    usuario = senha = ""
    while usuario == senha:
        usuario = input("Informe o nome de usuário: ")
        senha = input("Informe a senha: ")
        if usuario == senha:
            print("Erro: A senha não pode ser igual ao nome de usuário.")

    print("Usuário e senha válidos!")

pedir_credenciais()