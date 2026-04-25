# Exercício 16: Lê um valor n inteiro e positivo e calcula a soma S = 1 + 1/2 + 1/3 + ... + 1/n. Mostra cada termo e o valor final de S.

n = int(input("Digite um valor inteiro e positivo: "))

termo = 1
soma = 0.0
while (termo <= n):
    valor_termo = 1.0 / termo
    print(f"1/{termo} = {valor_termo}")
    soma = soma + valor_termo
    termo = termo + 1

print(f"Valor final de S: {soma}")