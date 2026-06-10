def achaMenor(vetor):
    menor = vetor[0]
    for i in range(len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]
    return menor

def ordenaVetor(vetor):
    vetorOrdenado = []
    for i in range(len(vetor)):
        menor = achaMenor(vetor)
        vetorOrdenado.append(menor)
        vetor.remove(menor)
    return vetorOrdenado

vetor = [1, 7, 4, 2, 8, 10, 3, 6, 5, 9, 11]

print(ordenaVetor(vetor))