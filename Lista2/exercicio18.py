# Exercício 18: Escreva um programa que receba dois números reais e um código de seleção do usuário. 
# Se o código digitado for 1, faça o programa adicionar os dois números previamente digitados e mostrar o resultado; 
# se o código de seleção for 2, os números devem ser multiplicados; 
# se o código de seleção for 3, o primeiro número deve ser dividido pelo segundo. 
# Se nenhuma das opções acima for escolhida, mostrar "Código inválido".

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
codigo = int(input("Digite o código de seleção: "))

if (codigo == 1):
    resultado = num1 + num2
    print(f"Soma: {resultado}")

else:
    if (codigo == 2):
        resultado = num1 * num2
        print(f"Multiplicação: {resultado}")

    else:
        if (codigo == 3):
            if num2 != 0:
                resultado = num1 / num2
                print(f"Divisão: {resultado}")
                
            else:
                print("Divisão por zero")
        else:
            print("Código inválido")