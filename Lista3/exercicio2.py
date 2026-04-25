# Exercício 2: Escreva um algoritmo que leia 20 valores e encontre o maior e o menor deles. Mostre o resultado.

valor = float(input("Digite o valor 1: "))
maior = valor
menor = valor

for i in range(1, 20):
    valor = float(input(f"Digite o valor {i + 1}: "))
    if (valor > maior):
        maior = valor
    if (valor < menor):
        menor = valor

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")