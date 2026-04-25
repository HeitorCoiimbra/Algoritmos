# Exercício 7: Efetuar a leitura do número de quilowatts consumidos e calcular o valor a ser pago de energia elétrica, sabendo-se que o valor a pagar por quilowatt é de 0,12. Apresentar o valor total a ser pago pelo usuário acrescido de 18% de ICMS.

kwh = float(input("Digite o número de quilowatts consumidos: "))
valor_kwh = kwh * 0.12
icms = valor_kwh * 0.18
total_pagar = valor_kwh + icms
print(f"Valor total a pagar: {total_pagar}")