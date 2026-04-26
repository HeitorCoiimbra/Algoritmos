# Exercício 20: Desenvolva um algoritmo para que, dados dois valores inteiros entre 1 e 10 lidos, 
# calcule e imprima: a média dos números caso a soma deles for menor que 8, seu produto caso a soma seja igual a 8 
# ou a divisão do maior pelo menor caso a soma dos valores for maior que 8.

num1 = int(input("Digite o primeiro número (1-10): "))
num2 = int(input("Digite o segundo número (1-10): "))
soma = num1 + num2

if (soma < 8):
    media = (num1 + num2) / 2
    print(f"Média: {media}")
else:
    if (soma == 8):
        produto = num1 * num2
        print(f"Produto: {produto}")
    else:
        if (num1 > num2):
            maior = num1
            menor = num2
        else:
            maior = num2
            menor = num1
        divisao = maior / menor
        print(f"Divisão do maior pelo menor: {divisao}")