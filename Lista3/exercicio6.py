# Exercício 6: Construir um algoritmo que calcule a média aritmética de vários valores inteiros positivos,
# digitados pelo usuário. O final da leitura acontecerá quando for lido um valor negativo.

valor = int(input("Digite um valor inteiro positivo (negativo para encerrar): "))

soma = 0
contagem = 0
while (valor >= 0):
    soma = soma + valor
    contagem = contagem + 1
    valor = int(input("Digite um valor inteiro positivo (negativo para encerrar): "))

if (contagem > 0):
    media = soma / contagem
else:
    media = 0

print(f"Média dos valores positivos: {media}")
print(f"Quantidade de valores lidos: {contagem}")