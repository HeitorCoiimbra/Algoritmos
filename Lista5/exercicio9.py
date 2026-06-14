# 9.	Implemente uma função que retorne a média dos valores armazenados em um vetor de inteiros.

def calcular_media(vetor):
    if len(vetor) > 0:
        soma = 0
        for i in range(len(vetor)):
            soma += vetor[i]
        media = soma / len(vetor)
        return media
    else:
        return 0

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(calcular_media(vetor))