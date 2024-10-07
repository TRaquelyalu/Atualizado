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
    # Valida o nome
    nome = ""
    while len(nome) <= 3:
        nome = input("Informe um nome (mais de 3 caracteres): ")
        if len(nome) <= 3:
            print("Erro: O nome deve ter mais de 3 caracteres.")
    
    # Valida a idade
    idade = -1
    while idade < 0 or idade > 150:
        idade = int(input("Informe uma idade (entre 0 e 150): "))
        if idade < 0 or idade > 150:
            print("Erro: A idade deve estar entre 0 e 150.")
    
    # Valida o salário
    salario = 0
    while salario <= 0:
        salario = float(input("Informe um salário (maior que 0): "))
        if salario <= 0:
            print("Erro: O salário deve ser maior que zero.")
    
    # Valida o sexo
    sexo = ""
    while sexo not in ['f', 'm']:
        sexo = input("Informe o sexo ('f' para feminino ou 'm' para masculino): ").lower()
        if sexo not in ['f', 'm']:
            print("Erro: O sexo deve ser 'f' ou 'm'.")
    
    # Valida o estado civil
    estado_civil = ""
    while estado_civil not in ['s', 'c', 'v', 'd']:
        estado_civil = input("Informe o estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo, 'd' para divorciado): ").lower()
        if estado_civil not in ['s', 'c', 'v', 'd']:
            print("Erro: O estado civil deve ser 's', 'c', 'v' ou 'd'.")
    
    # Mostra as informações válidas
    print("\nInformações válidas:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: R${salario}")
    print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
    print(f"Estado Civil: {estado_civil.upper()}")

validar_informacoes()
