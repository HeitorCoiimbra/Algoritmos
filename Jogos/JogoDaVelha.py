#Funções Gerais
def mostrarTabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        print(tabuleiro[i][0], " | " , tabuleiro[i][1], " | ", tabuleiro[i][2])
    return 

def verificaLinha(simbolo, linha, tabuleiro):
    quantidade = 0
    for j in range(len(tabuleiro[linha])):
        if (tabuleiro[linha][j] == simbolo):
            quantidade += 1

    if (quantidade == 3):
        return "venceu"
    else:
        return ""

def verificaColuna(simbolo, coluna, tabuleiro):
    quantidade = 0
    for i in range(len(tabuleiro)):
        if (tabuleiro[i][coluna] == simbolo):
            quantidade += 1

    if (quantidade == 3):
        return "venceu"
    else:
        return ""

def verificaDiagonal(simbolo, linha, coluna, tabuleiro):
    quantidade = 0
    if ((linha == 0 and coluna == 0) or (linha == 2 and coluna == 2)):
        for i in range(len(tabuleiro)):
            if (tabuleiro[i][i] == simbolo):
                quantidade += 1
    else:
        for i in range(len(tabuleiro)):
            if (tabuleiro[-i][-i] == simbolo):
                quantidade += 1

    if (quantidade == 3):
        return "venceu"
    else:
        return ""

def verificarVitoria(simbolo, tabuleiro, quem):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):

            if (tabuleiro[i][j] == simbolo):
                if verificaLinha(simbolo, i, tabuleiro) == "venceu":
                    return quem
                else:

                    if (verificaColuna(simbolo, j, tabuleiro) == "venceu"):
                        return quem
                    else:
                        if ((i == 0 or i == 2) and (j == 0 or j == 2)):
                            if (verificaDiagonal("X", i, j, tabuleiro) == "venceu"):
                                return quem
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

#Máquina
def rodadaMaquina():
    return

vencedor = ""
continuarRodada = True
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
mostrarTabuleiro(tabuleiro)
while continuarRodada:
    #Mostra tabuleiro
    

    #Jogador
    linha = int(input("Em qual linha deseja jogar?\n"))
    while linha > 2 or linha < 0:
        print("Linha inválida")
        linha = int(input("Em qual linha deseja jogar?\n"))

    coluna = int(input("Em qual coluna deseja joga?\n"))
    while coluna > 2 or coluna < 0:
        print("Coluna inválida")
        coluna = int(input("Em qual coluna deseja joga?\n"))
        
    resultadoJogada = registrarJogada(linha, coluna, tabuleiro)
    if not (resultadoJogada == ""): print(resultadoJogada)
    
    vencedor = verificarVitoria("X", tabuleiro, "Jogador")
    
    rodadaMaquina()
    mostrarTabuleiro(tabuleiro)
    if not (vencedor == ""): continuarRodada = False
print(f"A partida acabou e o vencedor foi {vencedor}!")