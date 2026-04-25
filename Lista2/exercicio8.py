# Exercício 8: Faça a leitura do ano atual e do ano de nascimento de uma pessoa e exibir sua idade. A seguir, informe se a pessoa é bebê (0 a 3 anos), criança (4 a 11 anos), adolescente (12 a 17 anos), adulta (18 a 64 anos) ou idosa (65 anos em diante).

ano_atual = int(input("Digite o ano atual: "))
ano_nasc = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nasc
print(f"Idade: {idade}")
if (idade <= 3):
    print("BEBÊ")
else:
    if (idade <= 11):
        print("CRIANÇA")
    else:
        if (idade <= 17):
            print("ADOLESCENTE")
        else:
            if (idade <= 64):
                print("ADULTA")
            else:
                print("IDOSA")