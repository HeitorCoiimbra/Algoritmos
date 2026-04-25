# Exercício 4: A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos.

salario = float(input("Digite o salário (negativo para encerrar): "))

soma_salarios = 0.0
soma_filhos = 0
quantidade = 0
maior_salario = 0.0
contador_ate_1000 = 0
while (salario >= 0):
    filhos = int(input("Digite o número de filhos: "))
    soma_salarios = soma_salarios + salario
    soma_filhos = soma_filhos + filhos
    quantidade = quantidade + 1
    if (salario > maior_salario):
        maior_salario = salario
    if (salario <= 1000):
        contador_ate_1000 = contador_ate_1000 + 1
    salario = float(input("Digite o salário (negativo para encerrar): "))

if (quantidade > 0):
    media_salario = soma_salarios / quantidade
    media_filhos = soma_filhos / quantidade
    percentual_ate_1000 = contador_ate_1000 * 100 / quantidade
else:
    media_salario = 0
    media_filhos = 0
    percentual_ate_1000 = 0

print(f"Média do salário: {media_salario}")
print(f"Média do número de filhos: {media_filhos}")
print(f"Maior salário: {maior_salario}")
print(f"Percentual até R$1000,00: {percentual_ate_1000}%")