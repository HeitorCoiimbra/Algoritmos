#1. Faça uma função que recebe, por parâmetro, uma matriz 5x5 e retorna a soma dos seus elementos.

def somaMatriz(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
    return soma


matriz = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
    ]

print(somaMatriz(matriz))