
def defineMaior(valores):
    maior = valores[0]

    for i in range(len(valores)):
        if valores[i] > maior:
            maior = valores[i]

    return maior

valores = []

for i in range(10):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

print(defineMaior(valores))