#7. Escrever uma função somarIntervalo(n1, n2) que retorna a soma dos números inteiros que existem entre n1 e n2 
# (inclusive ambos). A função deve funcionar inclusive se o valor de n2 for menor que n1. 

def somaIntervalos(n1, n2):
    soma = 0
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    for i in range(menor, maior + 1):
        soma += i
    return soma

n1 = int(input("Qual o valor de n1? "))
n2 = int(input("Qual o valor de n2? "))
soma = somaIntervalos(n1, n2)
print(f"A soma é {soma}")