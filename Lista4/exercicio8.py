#8. Escreva uma função que receba como parâmetro um valor n inteiro e positivo e que calcule a seguinte soma:
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n. A função deverá retornar o valor de S.

def calculaSoma(n):
    soma = 0
    for i in range(n):
        if i == 0:
            soma += 1
        else:
            soma += 1 / n
    return soma

n = int(input("Qual o valor de N? "))
soma = calculaSoma(n)
print(soma)