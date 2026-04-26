# Exercício 14: Desenvolva um algoritmo que leia o nome de um aluno, 
# suas notas em 2 provas e em um trabalho (todas com valores entre 0 e 10) e sua frequência, 
# definindo e imprimindo se ele foi aprovado, reprovado ou se fará prova final. 
# O aluno será reprovado se faltou mais de 15 aulas. 
# Será aprovado se não for reprovado por falta e sua média for maior ou igual a 6,0. 
# Caso tenha média menor, deverá fazer prova final. 
# O cálculo da média deve ser feito com peso 3 para a primeira prova, 5 para a segunda prova e 2 para o trabalho.

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
trabalho = float(input("Digite a nota do trabalho: "))
faltas = int(input("Digite o número de faltas: "))
if faltas > 15:
    print("REPROVADO por faltas")
else:
    media = (nota1 * 3 + nota2 * 5 + trabalho * 2) / (3 + 5 + 2)
    if media >= 6.0:
        print("APROVADO")
    else:
        print("FAZ PROVA FINAL")