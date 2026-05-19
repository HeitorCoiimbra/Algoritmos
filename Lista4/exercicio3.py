#3. Faça uma função que recebe por parâmetro o raio de uma esfera e calcule o seu volume (v = (4 x pi x R3)/3). 
def calculaVolumeEsfera(raio):
    return ((4 * 3.14 * (raio ** 3)) / 3)

raio = float(input("Qual o raio da esfera? "))
volume = calculaVolumeEsfera(raio)
print(f"O volume dessa esfera é: {volume}")