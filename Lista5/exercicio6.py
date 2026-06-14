# 6.	Escrever a função que recebe por parâmetro uma string e um número. A função deve retornar os primeiros 
# caracteres da string de acordo com o número passado por parâmetro.

def exibir_primeiros_caracteres(texto, numero):
    if numero > len(texto):
        numero = len(texto)
    retorno = ""
    for i in range(numero):
        retorno += texto[i]
    return retorno

print(exibir_primeiros_caracteres("UniAcademia", 12))