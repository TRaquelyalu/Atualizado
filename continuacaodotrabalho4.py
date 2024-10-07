def calcular_anos():
    while True:
        # Entrada das populações e taxas de crescimento
        populacao_a = int(input("População inicial do país A: "))
        populacao_b = int(input("População inicial do país B: "))
        taxa_a = float(input("Taxa de crescimento do país A (%): ")) / 100
        taxa_b = float(input("Taxa de crescimento do país B (%): ")) / 100

        # Calcula o número de anos necessários
        anos = 0
        while populacao_a < populacao_b:
            populacao_a += populacao_a * taxa_a
            populacao_b += populacao_b * taxa_b
            anos += 1

        print(f"Serão necessários {anos} anos para a população de A ultrapassar ou igualar a de B.")

        

calcular_anos()