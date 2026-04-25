# Exercício 3: Faça um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o fatorial de N (N!).

n = int(input("Digite um valor inteiro e positivo: "))
fatorial = 1

i = 1
while (i <= n):
    fatorial = fatorial * i
    i = i + 1

print(f"Fatorial de {n}: {fatorial}")