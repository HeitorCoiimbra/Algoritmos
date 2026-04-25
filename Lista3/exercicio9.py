# Exercício 9: Escrever o algoritmo que leia os valores n1 e n2 e imprima o intervalo fechado entre esses dois valores.

n1 = int(input("Digite o valor n1: "))
n2 = int(input("Digite o valor n2: "))

if (n1 <= n2):
    inicio = n1
    fim = n2
else:
    inicio = n2
    fim = n1

valor = inicio
while (valor <= fim):
    print(valor)
    valor = valor + 1