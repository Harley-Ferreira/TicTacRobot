from jogo.LogicaDoJogo import *

jogador = 0

# INSTÂNCIA DAS FUNÇÕES
matriz = tabuleiro()
ganhador = verificaGanhador(matriz)

# ENQUANTO NINGUEM GANHAR, EXECUTA
while not ganhador:
    # EXIBE O JOGO
    printTabu(matriz)

    # ESCOLHE A LINHA E COLUNA DA PEÇA
    i = saidaValida("Digite a linha: ")
    j = saidaValida("Digite a coluna: ")

    # VERIFICA O MOVIMENTO PARA SABER SE É VALIDO, ENTÃO ELE EXECUTA
    if verificaMovimento(matriz, i, j):
        fazMovimento(matriz, i, j, jogador)
        # SE O JOGADOR FOR 0 => (0 + 1)%2 = 1%2 = 1
        # SE O JOGADOR FOR 1 => (1 + 1)%2 = 2%2 = 0
        jogador = (jogador + 1) % 2
    else:
        print("Jogada Inválida")
    ganhador = verificaGanhador(matriz)

printTabu(matriz)
print("Ganhador = ", ganhador)