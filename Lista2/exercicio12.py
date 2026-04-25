# Exercício 12: A taxa de juros aplicada em fundos depositados em um banco é determinada pelo tempo em que estes ficam depositados. Para um banco em particular, a seguinte tabela é usada: ... (tabela omitida para brevidade)

tempo = float(input("Digite o tempo em depósito (anos): "))
if (tempo >= 5):
    taxa = 0.95
else:
    if (tempo >= 4):
        taxa = 0.90
    else:
        if (tempo >= 3):
            taxa = 0.85
        else:
            if (tempo >= 2):
                taxa = 0.75
            else:
                if (tempo >= 1):
                    taxa = 0.65
                else:
                    taxa = 0.55
print(f"Taxa de juros: {taxa}")