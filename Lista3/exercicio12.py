# Exercício 12: Leia uma quantidade desconhecida de números e conte quantos deles estão nos 
# intervalos [0,25], [26,50], [51,75] e [76,100]. A entrada termina quando for lido um número negativo.

valor = float(input("Digite um número (negativo para encerrar): "))

cont_0_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0
while (valor >= 0):
    if ((valor >= 0) and (valor <= 25)):
        cont_0_25 = cont_0_25 + 1
    else:
        if ((valor >= 26) and (valor <= 50)):
            cont_26_50 = cont_26_50 + 1
        else:
            if ((valor >= 51) and (valor <= 75)):
                cont_51_75 = cont_51_75 + 1
            else:
                if ((valor >= 76) and (valor <= 100)):
                    cont_76_100 = cont_76_100 + 1
    valor = float(input("Digite um número (negativo para encerrar): "))

print(f"Intervalo [0,25]: {cont_0_25}")
print(f"Intervalo [26,50]: {cont_26_50}")
print(f"Intervalo [51,75]: {cont_51_75}")
print(f"Intervalo [76,100]: {cont_76_100}")