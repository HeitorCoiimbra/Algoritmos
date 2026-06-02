
def ordenaVetor(valores):
    posicao = 0
    valoresOrdenados = []
    for i in range(len(valores)):
        atual = valores[i]

        for j in range(posicao, len(valores)):
            lugarCerto = True
            if atual > valores[j]:
                lugarCerto = False
        
        if lugarCerto:
            valoresOrdenados.append(atual)
    return valoresOrdenados

valores = [3,2,1]

print(ordenaVetor(valores))
