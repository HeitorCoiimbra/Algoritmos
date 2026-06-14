# 7.	Escrever a função que recebe por parâmetro uma string e um caracter. e a função deve retornar os 
# primeiros caracteres da string até encontrar o caracter passado por parâmetro.

def exibir_ate_um_caracter(texto, caracter):
    retorno = ""
    achar = False
    posicao = 0
    while not achar and posicao <= len(texto) - 1:
        retorno += texto[posicao]
        if texto[posicao] == caracter:
            achar = True
        posicao += 1
    return retorno

print(exibir_ate_um_caracter("UniAcademia", "x"))