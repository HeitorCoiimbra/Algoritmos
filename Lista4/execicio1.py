def calculaDias(anos, meses, dias):
    return anos * 365 + meses * 30 + dias 

anos = int(input("Qual a quantidade de anos? "))
meses = int(input("Qual a quantidade de meses? "))
dias = int(input("Qual a quantidade de dias? "))
resultado = calculaDias(anos, meses, dias)

print(resultado)