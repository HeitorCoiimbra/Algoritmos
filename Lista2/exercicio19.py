# Exercício 19: Faça um algoritmo que transforme a nota de um aluno em conceito. As notas 10 e 9 receberão conceito A, as notas 8 e 7 receberão conceito B, as notas 6 e 5 receberão conceito C e abaixo de 5 conceito D.

nota = float(input("Digite a nota: "))
if (nota >= 9):
    conceito = "A"
else:
    if (nota >= 7):
        conceito = "B"
    else:
        if (nota >= 5):
            conceito = "C"
        else:
            conceito = "D"
print(f"Conceito: {conceito}")