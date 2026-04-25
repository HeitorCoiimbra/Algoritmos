# Exercício 17: Lê 10 valores, um de cada vez, e conta quantos deles estão no intervalo [10,20] e quantos estão fora do intervalo.

cont_dentro = 0
cont_fora = 0

for i in range(10):
    valor = float(input(f"Digite o valor {i + 1}: "))
    if ((valor >= 10) and (valor <= 20)):
        cont_dentro = cont_dentro + 1
    else:
        cont_fora = cont_fora + 1

print(f"Quantidade no intervalo [10,20]: {cont_dentro}")
print(f"Quantidade fora do intervalo: {cont_fora}")