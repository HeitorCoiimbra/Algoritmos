# Exercício 18: Escrever um algoritmo que gere e escreva os 3 primeiros números perfeitos.

quant_encontrados = 0
numero = 2

while (quant_encontrados < 3):
    soma_divisores = 0
    divisor = 1
    while (divisor < numero):
        if ((numero % divisor) == 0):
            soma_divisores = soma_divisores + divisor
        divisor = divisor + 1
    if (soma_divisores == numero):
        print(numero)
        quant_encontrados = quant_encontrados + 1
    numero = numero + 1