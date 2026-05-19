#5. Escrever uma função verificarEstacao(dia, mes), que retorna qual a estação do ano da data passada por parâmetro.
# Lembrando que a primavera começa no dia 23 de setembro, o verão em 21 de dezembro, 
# o outono em 21 de março e o inverno em 21 de junho

def verificaEstacao(dia, mes):
    if (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia < 21):
        return "Outono"
    else:
        if (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia < 23):
            return "Inverno"
        else:
            if (mes == 9 and dia >= 23) or (mes > 9 and mes < 12) or (mes == 12 and dia < 21):
                return "Primavera"
            else:
                return "Verão"

dia = int(input("Qual o dia? "))
mes = int(input("Qual o mes (em número)? "))
estacao = verificaEstacao(dia, mes)
print(f"A estação dessa data é: {estacao}")