# 2. Faça uma função que recebe, por parâmetro, uma matriz 6x6 e retorna a soma dos elementos da sua diagonal 
# principal e da sua diagonal secundária

def somaDiagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

matriz = [
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6]
]

print(somaDiagonal(matriz))