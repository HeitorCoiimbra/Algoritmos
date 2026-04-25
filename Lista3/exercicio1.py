# Exercício 1: Escrever um algoritmo que lê 10 valores e conte quantos destes valores são negativos, escrevendo esta informação.

contador = 0

for i in range(10):
    valor = float(input(f"Digite o valor {i + 1}: "))
    if (valor < 0):
        contador = contador + 1

print(f"Quantidade de valores negativos: {contador}")