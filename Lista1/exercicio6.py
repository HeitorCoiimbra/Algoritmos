# Exercício 6: Calcular o salário líquido do funcionário sabendo que este é constituído pelo 
# salário bruto mais o valor das horas extras subtraindo 8% de INSS do total. 
# Serão lidos nesse problema o salário bruto, o valor das horas extras e o número de horas extras. 
# Apresentar ao final o salário líquido.

salario_bruto = float(input("Digite o salário bruto: "))
valor_hora_extra = float(input("Digite o valor das horas extras: "))
num_horas_extras = float(input("Digite o número de horas extras: "))
total_horas_extras = valor_hora_extra * num_horas_extras
total = salario_bruto + total_horas_extras
inss = total * 0.08
salario_liquido = total - inss
print(f"Salário líquido: {salario_liquido}")