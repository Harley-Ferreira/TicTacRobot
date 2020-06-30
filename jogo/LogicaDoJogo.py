from braco.ConverteCoordenadaParaAngulo import conversor
from braco.ConexaoRaspArduino import enviar

# CONDIÇÕES DO JOGO
peças = ["X", "O"]
espaço = " "


# LINHA = i
# COLUNA = j
coordenadas = {'33': [-6,  6], '32': [-6,  18], '31': [-6, 30],
               '21': [-18, 6], '22': [-18, 18], '23': [-18, 30],
               '13': [-30, 6], '12': [-30, 18], '11': [-30, 30]}

def criarmatriz():
    matriz = [
        [espaço, espaço, espaço],
        [espaço, espaço, espaço],
        [espaço, espaço, espaço],
    ]
    return matriz


def printmatriz(matriz):
    # PEGA A MATRIZ E DIVIDE EM 3 COLUNAS E 3 LINHAS
    print('----------------')
    print('| ' + str(matriz[0][0]) + ' || ' + str(matriz[0][1]) + ' || ' + str(matriz[0][2]) + ' |')
    print('----------------')
    print('| ' + str(matriz[1][0]) + ' || ' + str(matriz[1][1]) + ' || ' + str(matriz[1][2]) + ' |')
    print('----------------')
    print('| ' + str(matriz[2][0]) + ' || ' + str(matriz[2][1]) + ' || ' + str(matriz[2][2]) + ' |')
    print('----------------')


# VERIFICA OS VALORES ENTRADOS PARA COLUNA E LINHA
def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if (n >= 1 and n <= 3):
            return n - 1
        else:
            print("Numero precisa estar entra 1 e 3")
            return getInputValido(mensagem)
    except:
        print("Numero nao valido")
        return getInputValido(mensagem)


def verificaMovimento(matriz, i, j):
    if (matriz[i][j] == espaço):
        return True
    else:
        return False


def fazMovimento(matriz, i, j, jogador):
    matriz[i][j] = peças[jogador]

    s = str(i+1) + str(j+1)
    c = coordenadas[s]
    x = c[0]
    y = c[1]

    if jogador == 0:
        print("IA MOVEU O BRAÇO PARA")
        angulos = conversor(x, y, 36, 36)
        print(angulos)
        enviar(angulos[0], angulos[1])


def verificaGanhador(matriz):
    # linhas
    for i in range(3):
        if (matriz[i][0] == matriz[i][1] and matriz[i][1] == matriz[i][2] and matriz[i][0] != espaço):
            return matriz[i][0]

    # coluna
    for i in range(3):
        if (matriz[0][i] == matriz[1][i] and matriz[1][i] == matriz[2][i] and matriz[0][i] != espaço):
            return matriz[0][i]

    # diagonais
    if (matriz[0][0] != espaço and matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2]):
        return matriz[0][0]

    if (matriz[0][2] != espaço and matriz[0][2] == matriz[1][1] and matriz[1][1] == matriz[2][0]):
        return matriz[0][2]

    for i in range(3):
        for j in range(3):
            if (matriz[i][j] == espaço):
                return False

    return "EMPATE"

