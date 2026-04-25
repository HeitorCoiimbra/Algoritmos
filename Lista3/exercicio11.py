# Exercício 11: Leia um número não determinado de valores e calcule a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos.

valor = float(input("Digite um valor (0 para encerrar): "))

soma = 0
contagem = 0
cont_positivos = 0
cont_negativos = 0
while (valor != 0):
    soma = soma + valor
    contagem = contagem + 1
    if (valor > 0):
        cont_positivos = cont_positivos + 1
    else:
        cont_negativos = cont_negativos + 1
    valor = float(input("Digite um valor (0 para encerrar): "))

if (contagem > 0):
    media = soma / contagem
    percentual_positivos = cont_positivos * 100 / contagem
    percentual_negativos = cont_negativos * 100 / contagem
else:
    media = 0
    percentual_positivos = 0
    percentual_negativos = 0

print(f"Média: {media}")
print(f"Quantidade de positivos: {cont_positivos}")
print(f"Quantidade de negativos: {cont_negativos}")
print(f"Percentual de positivos: {percentual_positivos}%")
print(f"Percentual de negativos: {percentual_negativos}%")