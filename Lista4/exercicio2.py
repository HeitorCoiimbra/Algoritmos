#Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo:
# Nota         Conceito 
# De 0 a 49   =  D 
# De 50 a 69  =  C 
# De 70 a 89  =  B 
# De 90 a 100 =  A 

def conceitoMedia(media):
    if media < 50:
        return "D"
    else:
        if media < 70:
            return "C"
        else:
            if media < 90:
                return "B"
            else:
                return "A"


media = float(input("Qual a media do aluno? "))
if media > 100 or media < 0:
    print("Valor inválido")
else:
    conceito = conceitoMedia(media)
print(conceito)