# Exercício 16: Desenvolva um algoritmo que pergunte um código e de acordo com o valor digitado seja apresentado o cargo correspondente. Caso o usuário digite um código que não esteja na tabela, mostrar uma mensagem de código inválido. Utilize a tabela abaixo: ... (tabela omitida)

codigo = int(input("Digite o código: "))
if (codigo == 101):
    print("Vendedor")
else:
    if (codigo == 102):
        print("Atendente")
    else:
        if (codigo == 103):
            print("Auxiliar Técnico")
        else:
            if (codigo == 104):
                print("Assistente")
            else:
                if (codigo == 105):
                    print("Coordenador de Grupo")
                else:
                    if (codigo == 106):
                        print("Gerente")
                    else:
                        print("Código inválido")