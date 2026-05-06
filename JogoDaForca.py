continuarRodada = True
erros = 0

palavras = "a"
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
        palavraEscolhida = palavras
    else:
        palavraEscolhida = input("Qual palavra deve ser escolhida para a rodada? ")
        palavraEscolhidaLowercase = palavraEscolhida.lower()
    
    for i in range(len(palavraEscolhida)):
        if palavraEscolhida[i] not in letrasPalavraEscolhida:
            letrasPalavraEscolhida += palavraEscolhida[i]
    
    for i in range(len(palavraEscolhida)):
        palavraEscondida.append("_")


    while continuarRodada:
        letra = input("\nEscolha uma letra: ")

        if len(letra) != 1:
            print("Digite apenas uma letra!")
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

                else:
                    print("Errou paizão")
                    letrasErradas += letra
                    erros += 1
                    if erros >= 6: 
                        continuarRodada = False
                        print(f"Você foi enforcado! A palavra era: {palavraEscolhida}")
                    else:
                        print("".join(palavraEscondida))
        
        

        AcertouTodas = True
        for i in range(len(letrasPalavraEscolhida)):
            if letrasPalavraEscolhida[i].lower() not in letrasCertas.lower():
                AcertouTodas = False
        
        if AcertouTodas == True:
            continuarRodada = False
            print(f"Você achou a palavra! A palavra era: {palavraEscolhida}")