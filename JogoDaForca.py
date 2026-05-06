from random import *

continuarRodada = True
erros = 0

palavras = ["Zky", "Rszyzydkwy", "Kfsky", "Zkcckby", "Qkdy", "Mkmrybby", "Mkck", "Zybdk", "Myjsxrk", "Mknosbk", "Kbwkbsy", 
            "Vsfby", "Lsmsmvodk", "Mkbby", "Msnkno", "Wobmkny", "Cyv", "Vek", "Ocdbovk", "Xefow", "Mrefk", "Pyqy", "Kqek", 
            "Mywzedknyb", "Wydy", "Nyebkny", "Myxromswoxdy", "Nocdsxy", "Wkqscdbknk", "Klscwy", "Mkfkvosby", "Zobposdkwoxdo", 
            "Boxsdoxdo", "Mkbdk",  "Kmkmsk", "Oxobqsk", "Dowzy", "Zkbknyhy", "Wybdo", "Coxdswoxdy", "Sxdoxcsnkno", "Ckxqeo", 
            "Kvpklody", "Oqyscwy", "Xysdo", "Vklsbsxdy", "Oxsqwk", "Wony", "Nockccywlbkny", "Wowybsk", "Myvyccy", "Xysdo Coboxk", 
            "Ymevdy", "Csxy", "Dbkxcwsccky", "Bocoxrk", "Oczsbkv",  "Csxqevkb", "Oczobkxmk", "Rszxyco", "Ylbk-Zbswk", "Fkjsy", 
            "Csvoxmsy", "Pkxdkcwk", "Hknboj", "Wscdobsy", "Bokvsnkno", "Pbkqwoxdy", "Nkny"]

alfabeto = "KLMNOPQRSTUVWXYZABCDEFGHIJ"
palavraCodificada = ""
palavraDecodificada = ""

palavraEscolhida = ""
palavraEscolhidaLowercase = ""
palavraEscondida = []
letrasPalavraEscolhida = ""


letrasErradas = ""
letrasCertas = ""
letra = ""

formaEscolha = int(input("Como deve ser escolhida a palavra? \n1. Sorteio \n2. Escolha Manualmente\n"))
if formaEscolha > 2 or formaEscolha < 1:
    print("Escolha inválida")
else:

    if formaEscolha == 1:
        n = randint(0, (len(palavras) - 1))
        palavraCodificada = palavras[n].upper()

        for i in range(len(palavraCodificada)):
            if palavraCodificada[i] == " ":
                palavraEscolhida += " "
            else:

                if (palavraCodificada[i] == "-"):
                    palavraEscolhida += "-"

                else:
                    posicao = alfabeto.index(palavraCodificada[i])
                    if i == 0 or palavraCodificada[i - 1] == " " or palavraCodificada[i - 1] == "-":
                        palavraEscolhida += alfabeto[(posicao - 10) % 26]
                    else:
                        palavraEscolhida += alfabeto[(posicao - 10) % 26].lower()

    else:
        palavraEscolhida = input("Qual palavra deve ser escolhida para a rodada? ")
        palavraEscolhidaLowercase = palavraEscolhida.lower()
    
    for i in range(len(palavraEscolhida)):
        if palavraEscolhida[i] != " ":
            if palavraEscolhida[i] not in letrasPalavraEscolhida:
                letrasPalavraEscolhida += palavraEscolhida[i]
    
    for i in range(len(palavraEscolhida)):
        if palavraEscolhida[i] == " ":
            palavraEscondida.append(" ")
        else:
            if palavraEscolhida[i] == "-":
                palavraEscondida.append("-")
            else:
                palavraEscondida.append("_")
                
    print("".join(palavraEscondida))
    while continuarRodada:
        letra = input("\nEscolha uma letra: ").lower()

        if len(letra) > 1:
            print("Digite apenas uma letra!")
        else:
            if len(letra) < 1:
                print("Você deve jogar uma letra!")
            else:
                if letra in letrasErradas or letra in letrasCertas:
                    print("Você já jogou essa letra!")
                else:

                    if letra.lower() in palavraEscolhida.lower():
                        print(f"A palavra tem {letra}")
                        letrasCertas += letra

                        for i in range(len(palavraEscolhida)):
                            if palavraEscolhida[i].lower() == letra.lower():
                                palavraEscondida[i] = palavraEscolhida[i]
                        print("".join(palavraEscondida))
                        print(f"Erros: {erros}")
                        print(f"Letras erradas: {letrasErradas}")

                    else:
                        print("Essa letra não está na palavra")
                        letrasErradas += letra + " "
                        erros += 1
                        print("".join(palavraEscondida))
                        if erros >= 6: 
                            continuarRodada = False
                            print(f"Você foi enforcado! A palavra era: {palavraEscolhida}")
                        else:
                            print(f"Erros: {erros}")
                        print(f"Letras erradas: {letrasErradas}")
            
            

                    AcertouTodas = True
                    for i in range(len(letrasPalavraEscolhida)):
                        if letrasPalavraEscolhida[i] != " ":
                            if letrasPalavraEscolhida[i].lower() not in letrasCertas.lower():
                                AcertouTodas = False
                    
                    if AcertouTodas == True:
                        continuarRodada = False
                        print(f"\nVocê achou a palavra! A palavra era: {palavraEscolhida}")
