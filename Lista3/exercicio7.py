# Exercício 7: Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos.

codigo = int(input("Digite o código do voto (0 para encerrar): "))

votos1 = 0
votos2 = 0
votos3 = 0
votos4 = 0
votos_nulos = 0
votos_branco = 0
while (codigo != 0):
    if (codigo == 1):
        votos1 = votos1 + 1
    else:
        if (codigo == 2):
            votos2 = votos2 + 1
        else:
            if (codigo == 3):
                votos3 = votos3 + 1
            else:
                if (codigo == 4):
                    votos4 = votos4 + 1
                else:
                    if (codigo == 5):
                        votos_nulos = votos_nulos + 1
                    else:
                        if (codigo == 6):
                            votos_branco = votos_branco + 1
    codigo = int(input("Digite o código do voto (0 para encerrar): "))

print(f"Votos candidato 1: {votos1}")
print(f"Votos candidato 2: {votos2}")
print(f"Votos candidato 3: {votos3}")
print(f"Votos candidato 4: {votos4}")
print(f"Votos nulos: {votos_nulos}")
print(f"Votos em branco: {votos_branco}")