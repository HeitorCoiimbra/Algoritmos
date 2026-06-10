def ordenaVetorBolha(vetor):
    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            if vetor[j] < vetor[i]:
                aux = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = aux
    return vetor

def achaMenor(vetor):
    menor = vetor[0]
    for i in range(len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]
    return menor

def ordenaVetorMenor(vetor):
    vetorOrdenado = []
    for i in range(len(vetor)):
        menor = achaMenor(vetor)
        vetorOrdenado.append(menor)
        vetor.remove(menor)
    return vetorOrdenado

vetor = [1, 7, 4, 2, 8, 10, 3, 6, 5, 9, 11]

# print(ordenaVetorMenor(vetor))
print(ordenaVetorBolha(vetor))