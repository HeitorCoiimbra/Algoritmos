# Exercício 14: Uma empresa deseja aumentar seus preços em 20%. Leia o código e o preço de custo de cada produto
# e calcule o preço novo. A entrada termina quando for lido um código negativo.

codigo = int(input("Digite o código do produto (negativo para encerrar): "))

soma_preco_antigo = 0.0
soma_preco_novo = 0.0
contagem = 0

while (codigo >= 0):
    preco = float(input("Digite o preço de custo: "))
    preco_novo = preco * 1.20
    print(f"Código: {codigo}")
    print(f"Preço novo: {preco_novo}")

    soma_preco_antigo = soma_preco_antigo + preco
    soma_preco_novo = soma_preco_novo + preco_novo
    contagem = contagem + 1
    
    codigo = int(input("Digite o código do produto (negativo para encerrar): "))

if (contagem > 0):
    media_antigo = soma_preco_antigo / contagem
    media_novo = soma_preco_novo / contagem
else:
    media_antigo = 0
    media_novo = 0

print(f"Média dos preços sem aumento: {media_antigo}")
print(f"Média dos preços com aumento: {media_novo}")