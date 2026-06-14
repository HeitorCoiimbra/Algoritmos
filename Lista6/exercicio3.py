# 3. Faça uma função que recebe, por parâmetro, uma matriz 7x6 e retorna a soma dos elementos da 
# linha 5 e da coluna 3.

def somaLinhaEColuna(matriz, linha, coluna):
    somaLinha = 0
    somaColuna = 0

    for j in range(len(matriz[linha - 1])):
        somaLinha += matriz[linha - 1][j]

    for i in range(len(matriz)):
        somaColuna += matriz[i][coluna - 1]

    return somaLinha, somaColuna

matriz = [
    [1,1,1,1,1,1],
    [2,2,2,2,2,2],
    [3,3,3,3,3,3],
    [4,4,4,4,4,4],
    [5,5,5,5,5,5],
    [6,6,6,6,6,6],
    [7,7,7,7,7,7]
]

somaLinha, somaColuna = somaLinhaEColuna(matriz, 5, 3)
print(f"Soma da linha 5: {somaLinha} \nSoma da coluna 3: {somaColuna}\nSoma total: {somaColuna + somaLinha}")