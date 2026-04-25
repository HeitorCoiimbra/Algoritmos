# Exercício 13: Faça um algoritmo que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero.

valor = int(input("Digite um número positivo (0 para encerrar): "))

soma_total = 0
cont_total = 0
cont_pares = 0
soma_pares = 0
while (valor != 0):
    soma_total = soma_total + valor
    cont_total = cont_total + 1
    if ((valor % 2) == 0):
        cont_pares = cont_pares + 1
        soma_pares = soma_pares + valor
    valor = int(input("Digite um número positivo (0 para encerrar): "))

if (cont_total > 0):
    media_geral = soma_total / cont_total
else:
    media_geral = 0
if (cont_pares > 0):
    media_pares = soma_pares / cont_pares
else:
    media_pares = 0
cont_impares = cont_total - cont_pares

print(f"Quantidade de pares: {cont_pares}")
print(f"Quantidade de ímpares: {cont_impares}")
print(f"Média dos valores pares: {media_pares}")
print(f"Média geral: {media_geral}")