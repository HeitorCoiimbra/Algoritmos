# Exercício 10: Leia um número n que indica quantos valores devem ser lidos a seguir. Para cada número lido, mostre o valor lido e o fatorial deste valor.

n = int(input("Digite quantos valores serão lidos: "))

i = 1
while (i <= n):
    valor = int(input(f"Digite o valor {i}: "))
    fatorial = 1
    j = 1
    while (j <= valor):
        fatorial = fatorial * j
        j = j + 1
    print(f"Valor lido: {valor}")
    print(f"Fatorial: {fatorial}")
    i = i + 1