# Exercício 11: Escreva um programa para calcular e mostrar o salário semanal de uma pessoa, 
# determinado pelas condições que seguem. Se o número de horas trabalhadas for inferior ou igual a 40, 
# a pessoa recebe R$15,00 por hora, senão a pessoa recebe R$600,00 mais R$21,00 para cada hora trabalhada 
# acima de 40 horas. O programa deve pedir o número de horas trabalhadas como entrada e deve dar o salário como saída.

horas = float(input("Digite o número de horas trabalhadas: "))
if horas <= 40:
    salario = horas * 15
else:
    salario = 600 + (horas - 40) * 21
print(f"Salário semanal: R${salario}")