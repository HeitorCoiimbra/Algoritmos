from random import choice
#Funções Gerais
def mostrarTabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]}")
        if i < 2:
            print("---+---+---")
    return 

def verificarLinha(simbolo, linha, tabuleiro):
    quantidade = 0
    for j in range(len(tabuleiro[linha])):
        if (tabuleiro[linha][j] == simbolo):
            quantidade += 1

    if (quantidade == 3):
        return "venceu"
    else:
        return ""

def verificarColuna(simbolo, coluna, tabuleiro):
    quantidade = 0
    for i in range(len(tabuleiro)):
        if (tabuleiro[i][coluna] == simbolo):
            quantidade += 1

    if (quantidade == 3):
        return "venceu"
    else:
        return ""

def verificarDiagonal(simbolo, linha, coluna, tabuleiro):
    quantidade = 0
    if (linha == coluna):
        for i in range(len(tabuleiro)):
            if (tabuleiro[i][i] == simbolo):
                quantidade += 1
        
        if (quantidade == 3):
            return "venceu"
    
    quantidade = 0
    if ((linha + coluna) == 2):
        for i in range(len(tabuleiro)):
            if (tabuleiro[i][2 - i] == simbolo):
                quantidade += 1
        
        if (quantidade == 3):
            return "venceu"

    return ""

def verificarVelha(tabuleiro):
    vazios = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == " ":
                vazios += 1
    if (vazios == 0):
        return "Velha"
    else:
        return ""

def verificarVitoria(simbolo, tabuleiro, quem):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):

            if (tabuleiro[i][j] == simbolo):
                if verificarLinha(simbolo, i, tabuleiro) == "venceu":
                    return quem
                else:

                    if (verificarColuna(simbolo, j, tabuleiro) == "venceu"):
                        return quem
                    else:
                        if (((i == 0 or i == 2) and (j == 0 or j == 2)) or (i == 1 and j == 1)):
                            if (verificarDiagonal(simbolo, i, j, tabuleiro) == "venceu"):
                                return quem
                        
    if (verificarVelha(tabuleiro) == "Velha"):
        return "Velha"
    return ""

def registrarJogada(linha, coluna, tabuleiro, quem):
    if tabuleiro[linha][coluna] == " ":
        if (quem == "Jogador"):
            tabuleiro[linha][coluna] = "X"
        else:
            tabuleiro[linha][coluna] = "O"

        return ""
    else:
        return "Esse espaço já foi ocupado"

#Código
def verificarSePodeGanhar(tabuleiro, simbolo, quem):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if (tabuleiro[i][j] == " "):
                tabuleiro[i][j] = simbolo

                if (verificarVitoria(simbolo, tabuleiro, quem) == quem):
                    tabuleiro[i][j] = " "
                    return True, i, j
                else:
                    tabuleiro[i][j] = " "
    return False, -1, -1

def contarEspacosLivres(tabuleiro):
    espacosLivres = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if (tabuleiro[i][j] == " "):
                espacosLivres += 1

    return espacosLivres

def jogarLivremente(tabuleiro, codigoPrimeiro):
    linha = 0
    coluna = 0
    espacosLivres = contarEspacosLivres(tabuleiro)
    cantosLivres = []
    if tabuleiro[0][0] == " ":
        cantosLivres.append((0,0))
    if tabuleiro[0][2] == " ":
        cantosLivres.append((0,2))
    if tabuleiro[2][0] == " ":
        cantosLivres.append((2,0))
    if tabuleiro[2][2] == " ":
        cantosLivres.append((2,2))

    lateraisLivres = []
    if tabuleiro[0][1] == " ":
        lateraisLivres.append((0,1))
    if tabuleiro[1][0] == " ":
        lateraisLivres.append((1,0))
    if tabuleiro[1][2] == " ":
        lateraisLivres.append((1,2))
    if tabuleiro[2][1] == " ":
        lateraisLivres.append((2,1))
    
    # se comecei: canto -> canto contrario (se puder, ou outro canto) -> bloquear ou canto(o último) ou 
    # centro (se não tiver mais cantos) -> ganhar ou bloquear.
    if codigoPrimeiro:
        if espacosLivres > 1:
            for i in range(len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    if ((i == 0 or i == 2) and (j == 0 or j == 2)):
                        if ((tabuleiro[i][j] == "O") and (tabuleiro[2 - i][2 - j] == " ")):
                            linha = 2 - i
                            coluna = 2 - j
                            return linha, coluna 
                        
            linha, coluna = choice(cantosLivres)
            return linha, coluna
        
    else:
        #Se não comecei: Centro -> algum meio ->  ganhar, bloquear aleatório/canto(?)
        if (tabuleiro[1][1] == " "):
            linha = 1
            coluna = 1
            return linha, coluna
        else:
            if (len(cantosLivres) > 2):
                linha, coluna = choice(cantosLivres)
                return linha, coluna
            else:
                if (len(lateraisLivres) > 0):
                    linha, coluna = choice(lateraisLivres)
                    return linha, coluna
                else:
                    for i in range(len(tabuleiro)):
                        for j in range(len(tabuleiro[i])):
                            if (tabuleiro[i][j] == " "):
                                linha = i
                                coluna = j
                                return  linha, coluna
    
    return -1, -1

def rodadaMaquina(tabuleiro, codigoPrimeiro):
    #Ganhar
    possoGanhar, i, j = verificarSePodeGanhar(tabuleiro, "O", "Código")
    if possoGanhar:
        registrarJogada(i, j, tabuleiro, "Código")
        return i, j
    
        #Não perder
    possoPerder, i, j = verificarSePodeGanhar(tabuleiro, "X", "Jogador")
    if possoPerder:
        registrarJogada(i, j, tabuleiro, "Código")
        return i, j
    
        #"Aleatório"

    i, j = jogarLivremente(tabuleiro, codigoPrimeiro)
    registrarJogada(i, j, tabuleiro, "Código")
    return i, j

rodada = ""
vencedor = ""
continuarRodada = True
jogarNovamente = True
tabuleiro = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
            ]

while jogarNovamente:
    quemComeca = int(input("Quem deve começar? \n1)Jogador \n2)Código\n"))
    if (quemComeca == 1):
        rodada = "Jogador"
        codigoPrimeiro = False
    else:
        rodada = "Código"
        codigoPrimeiro = True

    mostrarTabuleiro(tabuleiro)
    
    while continuarRodada:   
        #Jogador
        if (rodada == "Jogador" and vencedor == ""):
            linha = int(input("Em qual linha deseja jogar?\n"))
            while linha > 2 or linha < 0:
                print("Linha inválida")
                mostrarTabuleiro(tabuleiro)
                linha = int(input("Em qual linha deseja jogar?\n"))

            coluna = int(input("Em qual coluna deseja jogar?\n"))
            while coluna > 2 or coluna < 0:
                print("Coluna inválida")
                mostrarTabuleiro(tabuleiro)
                coluna = int(input("Em qual coluna deseja jogar?\n"))
                
            resultadoJogada = registrarJogada(linha, coluna, tabuleiro, "Jogador")
            if not (resultadoJogada == ""): 
                print(resultadoJogada)
                mostrarTabuleiro(tabuleiro)
            else:
                vencedor = verificarVitoria("X", tabuleiro, "Jogador")
                rodada = "Código"
                mostrarTabuleiro(tabuleiro)

        #Código
        if (rodada == "Código" and vencedor == ""):
            i, j = rodadaMaquina(tabuleiro, codigoPrimeiro)
            vencedor = verificarVitoria("O", tabuleiro, "Código")
            print(f"\nO código jogou em ({i}, {j})")
            rodada = "Jogador"

            mostrarTabuleiro(tabuleiro)
        if not (vencedor == ""): continuarRodada = False

    if not (vencedor == ""):
        if not (vencedor == "Velha"):
            print(f"\nA partida terminou! O vencedor foi: {vencedor}")
        else:
            print("A partida terminou em Velha!")

    continuar = int(input("Deseja jogar novamente? \n1) Sim \n2) Não \n"))
    if (continuar == 2):
        print("Obrigado por jogar!")
        jogarNovamente = False
    else:
        if (continuar == 1):
            vencedor = ""
            continuarRodada = True
            for i in range(len(tabuleiro)):
                for j in range(len(tabuleiro[i])):
                    tabuleiro[i][j] = " "