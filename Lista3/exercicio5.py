# Exercício 5: Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,30 metro e cresce 3 centímetros por ano. Calcule quantos anos serão necessários para que Zé seja maior que Chico.

altura_chico = 1.50
altura_ze = 1.30
anos = 0

while (altura_ze <= altura_chico):
    altura_chico = altura_chico + 0.02
    altura_ze = altura_ze + 0.03
    anos = anos + 1

print(f"Serão necessários {anos} anos para Zé ficar maior que Chico.")