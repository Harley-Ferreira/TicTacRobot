import serial


def enviar(teta1, teta2):
    ang1 = str(teta1)
    ang2 = str(teta2)
    conexao = ""
    for porta in range(10):
        try:
            conexao = serial.Serial("COM" + str(porta), 115200)
            print("Conectado na porta: ", conexao.portstr)
            break
        except serial.SerialException:
            pass

    if conexao != "":
        resposta = conexao.read()
        if resposta == b'1':
            print(resposta)
            conexao.write(bytearray(ang1, 'utf-8'))
            resposta = conexao.read()
            if resposta == b'2':
                print(resposta)
                conexao.write(bytearray(ang2, 'utf-8'))
                resposta = conexao.read()
                print(resposta)
        conexao.close()
        print("Conexão encerrada")
    else:
        print("Sem portas disponíveis")
