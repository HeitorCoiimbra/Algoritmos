# Exercício 4: Calcular o aumento que será dado a um funcionário, 
# obtendo do usuário as seguintes informações: salário atual e a porcentagem de aumento. 
# Apresentar o novo valor do salário e o valor do aumento.

salario = float(input("Digite o salário atual: "))
porcentagem = float(input("Digite a porcentagem de aumento: "))
aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento
print(f"Novo salário: {novo_salario}")
print(f"Valor do aumento: {aumento}")