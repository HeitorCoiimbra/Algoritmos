# 4. Faça uma função que recebe, por parâmetro, uma matriz 6x6 e retorna o menor elemento da sua diagonal secundária.

def achaMenorDiagonal(matriz):
    menor = matriz[len(matriz) - 1][0]
    for i in range(len(matriz)):
        if matriz[-i][-i] < menor:
            menor = matriz[-i][-i]

    return menor

matriz = [
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6]
]

print(achaMenorDiagonal(matriz))