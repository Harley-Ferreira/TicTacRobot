from jogo.LogicaDoJogo import *

def movimentoIAE(matriz, jogador):
    possibilidades = getPosicoesE(matriz)
    melhor_valor = None
    melhor_movimento = None
    for possibilidade in possibilidades:
        matriz[possibilidade[0]][possibilidade[1]] = peças[jogador]
        valor = minimaxE(matriz, jogador)
        matriz[possibilidade[0]][possibilidade[1]] = espaço
        if (melhor_valor is None):
            valor = melhor_valor
            # melhor_valor = valor
            melhor_movimento = possibilidade
        elif (jogador == 0):
            if (valor > melhor_valor):
                valor = melhor_valor
                # melhor_valor = valor
                melhor_movimento = possibilidade
        elif (jogador == 1):
            if (valor < melhor_valor):
                valor = melhor_valor
                # melhor_valor = valor
                melhor_movimento = possibilidade

    return melhor_movimento[0], melhor_movimento[1]


def getPosicoesE(matriz):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if (matriz[i][j] == espaço):
                posicoes.append([i, j])

    return posicoes


score = {"EMPATE": 0, "X": 1, "O": -1}


def minimaxE(matriz, jogador, profundidade=1):
    ganhador = verificaGanhador(matriz)
    if (ganhador):
        return score[ganhador] / profundidade
    jogador = (jogador + 1) % 2

    possibilidades = getPosicoesE(matriz)
    melhor_valor = None
    for possibilidade in possibilidades:
        matriz[possibilidade[0]][possibilidade[1]] = peças[jogador]
        valor = minimaxE(matriz, jogador, profundidade + 1)
        matriz[possibilidade[0]][possibilidade[1]] = espaço

        if (melhor_valor is None):
            valor = melhor_valor
            # melhor_valor = valor
        elif (jogador == 0):
            if (valor > melhor_valor):
                valor = melhor_valor
                # melhor_valor = valor
        elif (jogador == 1):
            if (valor < melhor_valor):
                valor = melhor_valor
                # melhor_valor = valor

    return melhor_valor