# Exercício 15: Faça um algoritmo para verificar e imprimir entre 4 números lidos qual é o menor.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
menor = num1
if (num2 < menor):
    menor = num2
if (num3 < menor):
    menor = num3
if (num4 < menor):
    menor = num4
print(f"O menor número é: {menor}")