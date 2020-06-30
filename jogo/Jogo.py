from jogo.LogicaDoJogo import *
from inteligicia_articial.MinimaxEasy import *
from inteligicia_articial.MinimaxHard import *

jogador = 1
matriz = criarmatriz()
ganhador = verificaGanhador(matriz)
print("1- Fácil\n2- Impossível")
level = int(input("Escolha uma dificuldade dentre as opções: "))

if level == 1:
    while not ganhador:
        printmatriz(matriz)
        print("===================")
        if jogador == 0:
            i, j = movimentoIAE(matriz, jogador)
        else:
            i = getInputValido("Digite a linha: ")
            j = getInputValido("Digite a coluna: ")

        if (verificaMovimento(matriz, i, j)):
            fazMovimento(matriz, i, j, jogador)
            jogador = (jogador + 1) % 2
        else:
            print("A posicao informado ja esta ocupada")

        ganhador = verificaGanhador(matriz)

    print("===================")
    printmatriz(matriz)
    print("Ganhador = ", ganhador)
    print("===================")
elif level == 2:
    while not ganhador:
        printmatriz(matriz)
        print("===================")
        if jogador == 0:
            i,j = movimentoIAH(matriz, jogador)
        else:
            i = getInputValido("Digite a linha: ")
            j = getInputValido("Digite a coluna: ")

        if(verificaMovimento(matriz, i, j)):
            fazMovimento(matriz, i, j, jogador)
            jogador = (jogador + 1)%2
        else:
            print("A posicao informado ja esta ocupada")

        ganhador = verificaGanhador(matriz)

    print("===================")
    printmatriz(matriz)
    print("Ganhador = ", ganhador)
    print("===================")
else:
    pass