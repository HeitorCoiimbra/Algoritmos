# 5.	Escrever uma função que recebe por parâmetro um vetor de inteiros e retorna a soma de seus elementos.

def somar_elementos(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    return soma

vetor = [1, 2, 4, 5, 6]
print(somar_elementos(vetor))