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