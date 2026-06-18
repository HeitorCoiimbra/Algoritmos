from random import *

continuarJogando = True
continuarRodada = True

validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ3"

palavras = ["Zky", "Rszyzydkwy", "Kfsky", "Zkcckby", "Qkdy", "Mkmrybby", "Mkck", "Zybdk", "Myjsxrk", "Mknosbk", "Kbwkbsy", 
            "Vsfby", "Lsmsmvodk", "Mkbby", "Msnkno", "Wobmkny", "Cyv", "Vek", "Ocdbovk", "Xefow", "Mrefk", "Pyqy", "Kqek", 
            "Mywzedknyb", "Wydy", "Nyebkny", "Myxromswoxdy", "Nocdsxy", "Wkqscdbknk", "Klscwy", "Mkfkvosby", "Zobposdkwoxdo", 
            "Boxsdoxdo", "Mkbdk",  "Kmkmsk", "Oxobqsk", "Dowzy", "Zkbknyhy", "Wybdo", "Coxdswoxdy", "Sxdoxcsnkno", "Ckxqeo", 
            "Kvpklody", "Oqyscwy", "Xysdo", "Vklsbsxdy", "Oxsqwk", "Wony", "Nockccywlbkny", "Wowybsk", "Myvyccy", "Xysdo Coboxk", 
            "Ymevdy", "Csxy", "Dbkxcwsccky", "Bocoxrk", "Oczsbkv",  "Csxqevkb", "Oczobkxmk", "Rszxyco", "Ylbk-Zbswk", "Fkjsy", 
            "Csvoxmsy", "Pkxdkcwk", "Hknboj", "Wscdobsy", "Bokvsnkno", "Pbkqwoxdy", "Nkny", "Aeolbk-Mklomk", "Vek no ckxqeo", "Qekbnk-Mrefk"]

alfabeto = "KLMNOPQRSTUVWXYZABCDEFGHIJ"

while continuarJogando == True:
    palavraCodificada = ""
    palavraDecodificada = ""

    palavraEscolhida = ""
    palavraEscondida = []
    letrasPalavraEscolhida = ""

    letrasErradas = ""
    letrasCertas = ""
    letra = ""

    erros = 0
    
    formaEscolha = int(input("\nComo deve ser escolhida a palavra? \n1. Sorteio \n2. Escolha Manualmente\n"))
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
                    if letra.upper() not in validos:
                        print("Isso não é uma letra!")
                    else:
                        if letra in letrasErradas or letra in letrasCertas:
                            print("Você já jogou essa letra!")
                        else:
                            print("Digite 3 se quiser arriscar a plavra completa\n")
                            if letra != "3":
                                if letra.lower() in palavraEscolhida.lower():
                                    print(f"A palavra tem {letra.upper()}")
                                    letrasCertas += letra

                                    for i in range(len(palavraEscolhida)):
                                        if palavraEscolhida[i].lower() == letra.lower():
                                            palavraEscondida[i] = palavraEscolhida[i]
                                    

                                else:
                                    print(f"A {letra.upper()} não está na palavra")
                                    letrasErradas += letra + " "
                                    erros += 1
                                    
                            else:
                                confirma = int(input(f"Tem certeza que quer arriscar tudo em um chute? \n1. Sim \n2. Não \n"))
                                if confirma == 1:
                                    chute = input("Qual a palavra completa?\n")

                                    AcertouTodas = True
                                    for i in range(len(letrasPalavraEscolhida)):
                                        if letrasPalavraEscolhida[i] != " " and letrasPalavraEscolhida[i] != "-":
                                            if letrasPalavraEscolhida[i].lower() not in chute.lower():
                                                AcertouTodas = False
                                                erros = 10
                                    
                                    if AcertouTodas == True:
                                        letrasCertas += chute

                            if erros > 6: 
                                continuarRodada = False
                                print(f"\nVocê foi enforcado! A palavra era: {palavraEscolhida}")
                            else:
                                print("".join(palavraEscondida))
                                print(f"\nErros: {erros}")
                            print(f"Letras erradas: {letrasErradas}")
                            
                    

                            AcertouTodas = True
                            for i in range(len(letrasPalavraEscolhida)):
                                if letrasPalavraEscolhida[i] != " " and letrasPalavraEscolhida[i] != "-":
                                    if letrasPalavraEscolhida[i].lower() not in letrasCertas.lower():
                                        AcertouTodas = False
                            
                            if AcertouTodas == True:
                                continuarRodada = False
                                print(f"\nVocê achou a palavra! A palavra era: {palavraEscolhida}")
    continuar = 0
    while continuar > 2 or continuar < 1:
        continuar = int(input("\nDeseja jogar novamente? \n1. Sim \n2. Não \n"))
        if continuar > 2 or continuar < 1:
            print("Escolha inválida")
        else:
            if continuar == 1:
                continuarJogando = True
                continuarRodada = True

            else:
                continuarJogando = False
                print("\nObrigado por jogar!")