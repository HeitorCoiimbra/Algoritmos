from random import *

continuarRodada = True
erros = 0

palavras = "Zky|Rszyzydkwy|Kfsky|Zkcckby|Qkdy|Mkmrybby|Mkck|Zybdk|Myjsxrk|Mknosbk|Kbwkbsy" \
            "|Vsfby|Lsmsmvodk|Mkbby|Msnkno|Wobmkny|Cyv|Vek|Ocdbovk|Xefow|Mrefk|Pyqy|Kqek" \
            "|Mywzedknyb|Wydy|Nyebkny|Myxromswoxdy|Nocdsxy|Wkqscdbknk|Klscwy|Mkfkvosby|Zobposdkwoxdo" \
            "|Boxsdoxdo|Mkbdk|Kmkmsk|Oxobqsk|Dowzy|Zkbknyhy|Wybdo|Coxdswoxdy|Sxdoxcsnkno|Ckxqeo" \
            "|Kvpklody|Oqyscwy|Xysdo|Vklsbsxdy|Oxsqwk|Wony|Nockccywlbkny|Wowybsk|Myvyccy|Xysdo Coboxk" \
            "|Ymevdy|Csxy|Dbkxcwsccky|Bocoxrk|Oczsbkv|Csxqevkb|Oczobkxmk|Rszxyco|Ylbk-Zbswk|Fkjsy" \
            "|Csvoxmsy|Pkxdkcwk|Hknboj|Wscdobsy|Bokvsnkno|Pbkqwoxdy|Nkny"

alfabeto = "KLMNOPQRSTUVWXYZABCDEFGHIJ"
palavraEscolhida = ""
palavraCodificada = ""

palavraEscondida = ""
letrasPalavraEscolhida = ""

letrasErradas = ""
letrasCertas = ""

formaEscolha = int(input("Como deve ser escolhida a palavra? \n1. Sorteio \n2. Escolha Manualmente\n"))
if formaEscolha > 2 or formaEscolha < 1:
    print("Escolha inválida")
else:

    if formaEscolha == 1:
        quantidadePalavras = 1

        for i in range(len(palavras)):
            if palavras[i] == "|":
                quantidadePalavras += 1
        sorteio = randint(0, quantidadePalavras - 1)
        palavraAtual = 0
        palavraCodificada = ""

        for i in range(len(palavras)):
            if palavras[i] == "|":
                palavraAtual += 1
            else:

                if palavraAtual == sorteio:
                    palavraCodificada += palavras[i]
        palavraCodificada = palavraCodificada.upper()

        for i in range(len(palavraCodificada)):
            if palavraCodificada[i] == " ":
                palavraEscolhida += " "
            else:

                if palavraCodificada[i] == "-":
                    palavraEscolhida += "-"
                else:

                    posicao = alfabeto.index(palavraCodificada[i])
                    letraDecodificada = alfabeto[(posicao - 10) % 26]
                    if i == 0:
                        palavraEscolhida += letraDecodificada
                    else:

                        if palavraCodificada[i - 1] == " " or palavraCodificada[i - 1] == "-":
                            palavraEscolhida += letraDecodificada
                        else:
                            palavraEscolhida += letraDecodificada.lower()
    
    else:
        palavraEscolhida = input("Qual palavra deve ser escolhida para a rodada? ")

    for i in range(len(palavraEscolhida)):
        if palavraEscolhida[i] != " " and palavraEscolhida[i] != "-":
            if palavraEscolhida[i].lower() not in letrasPalavraEscolhida:
                letrasPalavraEscolhida += palavraEscolhida[i].lower()

    for i in range(len(palavraEscolhida)):
        if palavraEscolhida[i] == " ":
            palavraEscondida += " "
        else:
            if palavraEscolhida[i] == "-":
                palavraEscondida += "-"
            else:
                palavraEscondida += "_"

    print(palavraEscondida)
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

                    if letra in palavraEscolhida.lower():
                        print(f"A palavra tem {letra}")
                        letrasCertas += letra
                        novaPalavraEscondida = ""

                        for i in range(len(palavraEscolhida)):
                            if palavraEscolhida[i].lower() == letra:
                                novaPalavraEscondida += palavraEscolhida[i]
                            else:
                                novaPalavraEscondida += palavraEscondida[i]
                        palavraEscondida = novaPalavraEscondida
                        print(palavraEscondida)

                    else:
                        print("Essa letra não está na palavra")
                        letrasErradas += letra + " "
                        erros += 1
                        print(palavraEscondida)
                        if erros > 6:
                            continuarRodada = False
                            print(f"Você foi enforcado! A palavra era: {palavraEscolhida}")
                        else:
                            print(f"Erros: {erros}")
                        print(f"Letras erradas: {letrasErradas}")

                    AcertouTodas = True
                    for i in range(len(letrasPalavraEscolhida)):
                        if letrasPalavraEscolhida[i] not in letrasCertas:
                            AcertouTodas = False

                    if AcertouTodas == True:
                        continuarRodada = False
                        print(f"\nVocê achou a palavra! A palavra era: {palavraEscolhida}")