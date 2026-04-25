# Exercício 6: Ler um número e informar se ele é positivo, negativo ou neutro (zero).

num = float(input("Digite um número: "))
if num > 0:
    print("POSITIVO")
elif num < 0:
    print("NEGATIVO")
else:
    print("NEUTRO")