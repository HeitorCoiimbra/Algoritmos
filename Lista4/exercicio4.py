# 4. Escrever uma função contarImpar(n1, n2) que retorna o número de inteiros ímpares que existem entre n1 e n2 
# (inclusive ambos, se for o caso). A função deve funcionar inclusive se o valor de n2 for menor que n1.
def contaImpares(n1, n2):
    impares = ""
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1

    nAtual = menor
    while nAtual <= maior:
        if (nAtual % 2) != 0:
            impares += " " + str(nAtual)
        nAtual += 1
    return impares

n1 = int(input("Qual o valor de n1? "))
n2 = int(input("Qual o valor de n2? "))

impares = contaImpares(n1, n2)
print(f"Os números ímpares entre {n1} e {n2} são: {impares}")