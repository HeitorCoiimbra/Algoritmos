# 6. Escrever uma função calcularQuociente(dividendo, divisor), que  retorna a divisão inteira (sem casas decimais) 
# de dividendo por divisor e outra função  calcularResto(dividendo, divisor) que retorna o resto.

def calcularResto(dividendo, divisor):
    return dividendo % divisor

def calcularQuociente(dividendo, divisor):
    return dividendo // divisor

dividendo = int(input("Qual o dividendo? "))
divisor = int(input("Qual o divisor? "))
quociente = calcularQuociente(dividendo, divisor)
resto = calcularResto(dividendo, divisor)
print(f"O quociente é {quociente} e o resto é {resto}")