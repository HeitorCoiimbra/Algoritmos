# Exercício 5: Ler um número inteiro e testar se o valor lido termina com 0 (divisível por 10). Em caso positivo, exiba a metade deste número. Caso contrário, exibir a mensagem "O número digitado não termina com 0".

num = int(input("Digite um número inteiro: "))
if num % 10 == 0:
    metade = num // 2
    print(f"A metade é: {metade}")
else:
    print("O número digitado não termina com 0")