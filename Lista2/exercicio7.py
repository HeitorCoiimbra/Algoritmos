# Exercício 7: Faça a leitura do salário atual e do tempo de serviço de um funcionário. A seguir, calcule o seu salário reajustado. Funcionários com até 1 ano de empresa, receberão aumento de 10%. Funcionários com mais de um ano de tempo de serviço, receberão aumento de 20%.

salario = float(input("Digite o salário atual: "))
tempo = float(input("Digite o tempo de serviço (anos): "))
if tempo <= 1:
    aumento = 0.10
else:
    aumento = 0.20
novo_salario = salario * (1 + aumento)
print(f"Salário reajustado: {novo_salario}")