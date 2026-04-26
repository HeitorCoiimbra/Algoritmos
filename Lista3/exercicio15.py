# Exercício 15: Escreva um algoritmo que gere os números de 1000 a 1999 e escreva aqueles que divididos 
# por 11 dão resto igual a 5.

numero = 1000

while (numero <= 1999):
    resto = numero % 11
    if (resto == 5):
        print(numero)
    numero = numero + 1