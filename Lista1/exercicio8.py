# Exercício 8: Calcular a média de combustível gasto pelo usuário, sendo informado a quantidade de quilômetros rodados e a quantidade de combustível consumido.

km = float(input("Digite a quantidade de quilômetros rodados: "))
combustivel = float(input("Digite a quantidade de combustível consumido: "))
media = km / combustivel
print(f"Média de combustível: {media} km/l")