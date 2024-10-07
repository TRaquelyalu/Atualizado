'''
3.	Faça um programa que leia e valide as seguintes informações:
a.	Nome: maior que 3 caracteres;
b.	Idade: entre 0 e 150;
c.	Salário: maior que zero;
d.	Sexo: 'f' ou 'm';
e.	Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
'''
def validar_informacoes():
    nome = input("Informe o nome (mais de 3 caracteres): ")
    while len(nome) <= 3:
        nome = input("Erro: O nome deve ter mais de 3 caracteres. Tente novamente: ")
    
    idade = int(input("Informe a idade (entre 0 e 150): "))
    while idade < 0 or idade > 150:
        idade = int(input("Erro: A idade deve estar entre 0 e 150. Tente novamente: "))
    
    salario = float(input("Informe o salário (maior que 0): "))
    while salario <= 0:
        salario = float(input("Erro: O salário deve ser maior que zero. Tente novamente: "))
    
    sexo = input("Informe o sexo ('f' para feminino ou 'm' para masculino): ").lower()
    while sexo not in ['f', 'm']:
        sexo = input("Erro: O sexo deve ser 'f' ou 'm'. Tente novamente: ").lower()
    
    estado_civil = input("Informe o estado civil ('s', 'c', 'v', 'd'): ").lower()
    while estado_civil not in ['s', 'c', 'v', 'd']:
        estado_civil = input("Erro: O estado civil deve ser 's', 'c', 'v' ou 'd'. Tente novamente: ").lower()
    
    print("\nInformações válidas!")
    
validar_informacoes()