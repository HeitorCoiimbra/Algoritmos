# Exercício 2: Efetuar a leitura de uma nota e, se o valor for maior ou igual a 60, 
# imprimir na tela "APROVADO", se for menor, imprimir reprovado.

nota = float(input("Digite a nota: "))
if nota >= 60:
    print("APROVADO")
else:
    print("REPROVADO")