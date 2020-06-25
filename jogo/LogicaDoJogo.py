from braco.ConverteCoordenadaParaAngulo import conversor
from braco.ConexaoRaspArduino import enviar


# CONDIÇÕES DO JOGO
peças = ["X", "O"]
espaço = " "


# LINHA = i
# COLUNA = j

def tabuleiro():
    # GERA CADA CASA NO TABULEIRO
    matriz = [
        [espaço, espaço, espaço],
        [espaço, espaço, espaço],
        [espaço, espaço, espaço],
    ]
    return matriz


def printTabu(matriz):
    # PEGA A MATRIZ E DIVIDE EM 3 COLUNAS E 3 LINHAS
    for i in range(3):
        print('|'.join(matriz[i]))
        if i < 2:
            print("------")


# VERIFICA OS VALORES ENTRADOS PARA COLUNA E LINHA
def saidaValida(mensagem):
    try:
        n = int(input(mensagem))
        if n >= 1 and n <= 3:
            return n - 1

    except:
        saidaValida(mensagem)


def verificaMovimento(matriz, i, j):
    try:
        if matriz[i][j] == espaço:
            return True
        else:
            return False
    except:
        pass


def fazMovimento(matriz, i, j, jogador):
    matriz[i][j] = peças[jogador]
    #As variaveis IA, x e y devem ser preenchidas.
    IA = ""
    x = 0
    y = 0
    if IA == jogador:
        angulos = conversor(x, y, 150, 150)
        enviar(angulos[0], angulos[1])





def verificaGanhador(matriz):
    # VERIFICA O GANHADOR NA LINHA
    for i in range(3):
        if matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2] and matriz[i][0] != espaço:
            return matriz[i][0]

    # VERIFICA O GANHADOR NA LINHA
    for j in range(3):
        if matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i] and matriz[0][i] != espaço:
            return matriz[i][0]

    # VERIFICA O GANHADOR NAS DIAGONAIS
    if matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] and matriz[0][0] != espaço:
        return matriz[0][0]

    if matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0] and matriz[0][2] != espaço:
        return matriz[0][2]

    for i in range(3):
        for j in range(3):
            if matriz[i][j] == espaço:
                return False

    return "EMPATE"
