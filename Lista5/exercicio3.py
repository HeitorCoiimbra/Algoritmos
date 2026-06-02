
def defineMenor(valores):
    menor = valores[0]

    for i in range(len(valores)):
        if valores[i] < menor:
            menor = valores[i]

    return menor

valores = []

for i in range(10):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

print(defineMenor(valores))