# Exercício 8: Escrever um algoritmo que leia uma variável n e calcule a tabuada de 1 até n.

n = int(input("Digite o valor de n: "))

i = 1
while (i <= n):
    resultado = i * n
    print(f"{i} x {n} = {resultado}")
    i = i + 1