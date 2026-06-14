# 10.	Escrever uma função que substitui por zero todos os números negativos do vetor passado por parâmetro.

def substiuir_negativos(vetor):
    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor[i] = 0
    return vetor

vetor = [1, -2, 3, -4, 5]
print(substiuir_negativos(vetor))