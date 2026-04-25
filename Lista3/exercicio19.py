# Exercício 19: Leia um valor N inteiro e positivo e calcule o valor de E = 1 + 1/1! + 1/2! + ... + 1/N!.

n = int(input("Digite um valor inteiro e positivo: "))
fatorial = 1
termo = 1
soma = 1.0

while (termo <= n):
    fatorial = fatorial * termo
    soma = soma + 1.0 / fatorial
    termo = termo + 1

print(f"Valor de E: {soma}")