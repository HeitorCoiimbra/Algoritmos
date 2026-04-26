# Exercício 13: Baseado no ano e peso do modelo de um automóvel, o estado de Nova Jersey 
# determina a sua classe de peso e taxa de registro usando a seguinte tabela: ... (tabela omitida)

ano = int(input("Digite o ano do modelo: "))
peso = float(input("Digite o peso (kg): "))
if (ano <= 1970):
    if (peso < 1200):
        classe = 1
        taxa = 16.50
    else:
        if (peso <= 1700):
            classe = 2
            taxa = 25.50
        else:
            classe = 3
            taxa = 46.50
else:
    if (ano <= 1979):
        if (peso < 1200):
            classe = 4
            taxa = 27.00
        else:
            if (peso <= 1700):
                classe = 5
                taxa = 30.50
            else:
                classe = 6
                taxa = 52.50
    else:  # 1980 or after
        if (peso < 1600):
            classe = 7
            taxa = 19.50
        else:
            classe = 8
            taxa = 55.50
print(f"Classe: {classe}")
print(f"Taxa de registro: {taxa}")