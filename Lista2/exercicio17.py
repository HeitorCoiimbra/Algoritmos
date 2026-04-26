# Exercício 17: Uma encomenda de unidades de disco contém unidades marcadas com um código de 1 a 4, 
# que indica o tipo seguinte: ... (tabela omitida)

codigo = int(input("Digite o código: "))
if (codigo == 1):
    print("CD-ROM (700MB)")
else:
    if (codigo == 2):
        print("DVD-ROM (4.7GB)")
    else:
        if (codigo == 3):
            print("DVD-9 (8.54 GB)")
        else:
            if (codigo == 4):
                print("Blu-Ray (25 GB)")
            else:
                print("Código inválido")