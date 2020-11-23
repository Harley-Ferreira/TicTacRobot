import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver
#Captura dos Contornos

def getContorno(x):
    contorno,hierarquia = cv2.findContours(x,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contorno:
        area = cv2.contourArea(cnt)

        cv2.drawContours(x,cnt,-1,(255,0,0),4)
        return area

#Tratamento de Imagem
captura = cv2.imread("Resources/Tic_Tac_Robot.jpg")
capturaCinza = cv2.cvtColor(captura,cv2.COLOR_BGR2GRAY)
capturaBlur = cv2.GaussianBlur(capturaCinza,(13,13),2)
contornos = cv2.Canny(capturaBlur,40,80)
x = 0
y = 0



#Divisao de Imagem

space1 = captura[600:910, 0:500]
space2 = captura[600:910, 500:1000]
space3 = captura[600:910, 1000:1500]
space4 = captura[300:600, 0:500]
space5 = captura[300:600, 500:1000]
space6 = captura[300:600, 1000:1500]
space7 = captura[0:300, 0:500]
space8 = captura[0:300, 500:1000]
space9 = captura[0:300, 1000:1500]


spacec1 = captura[600+x:900+y, 10:500+y]
spacec2 = captura[600+x:900+y, 500+x:1000+y]
spacec3 = captura[600+x:900+y, 1000+x:1500+y]
spacec4 = captura[300+x:590+y, 10:500+y]
spacec5 = captura[300+x:590+y, 500+x:1000+y]
spacec6 = captura[300+x:590+y, 1000+x:1500+y]
spacec7 = captura[10:293+y, 0:500+y]
spacec8 = captura[10:290+y, 500+x:1000+y]
spacec9 = captura[5:293+y, 1000+x:1500+y]


#Criação de Matrizes

matrizx = [[0,0,0],[0,0,0],[0,0,0]]

matrizBolinha = [[0,0,0],[0,0,0],[0,0,0]]


sp7 = getContorno(space7)
sp8 = getContorno(space8)
sp9 = getContorno(space9)

if(sp7 == None):
    sp7 = 1
if(sp8 == None):
    sp7 = 1
if(sp9 == None):
    sp7 = 1

if(sp7>400 and sp7<450):
    matrizx[0][0] = 1
if(sp8>400 and sp8<450):
    matrizx[0][1] = 1
if(sp9>400 and sp9<450):
    matrizx[0][2] = 1

if(sp7>60000 and sp7<65000):
    matrizBolinha[0][0] = 1
if(sp8>60000 and sp8<65000):
    matrizBolinha[0][1] = 1
if(sp9>60000 and sp9<65000):
    matrizBolinha[0][2] = 1


sp4 = getContorno(space4)
sp5 = getContorno(space5)
sp6 = getContorno(space6)

if(sp4 == None):
    sp4 = 1
if(sp5 == None):
    sp5 = 1
if(sp6 == None):
    sp6 = 1

if(sp4>400 and sp4<450):
    matrizx[1][0] = 1
if(sp5>400 and sp5<450):
    matrizx[1][1] = 1
if(sp6>400 and sp6<450):
    matrizx[1][2] = 1

if (sp4 > 60000 and sp4 < 65000):
    matrizBolinha[1][0] = 1
if (sp5 > 60000 and sp5 < 65000):
    matrizBolinha[1][1] = 1
if (sp6 > 60000 and sp6 < 65000):
    matrizBolinha[1][2] = 1


sp1 = getContorno(space7)
sp2 = getContorno(space8)
sp3 = getContorno(space9)

if(sp1 == None):
    sp1 = 1
if(sp2 == None):
    sp2 = 1
if(sp3 == None):
    sp3 = 1

if(sp1>400 and sp1<450):
    matrizx[2][0] = 1
if(sp2>400 and sp2<450):
    matrizx[2][1] = 1
if(sp3>400 and sp3<450):
    matrizx[2][2] = 1

if (sp1 > 60000 and sp1 < 65000):
    matrizBolinha[2][0] = 1
if (sp2 > 60000 and sp2 < 65000):
    matrizBolinha[2][1] = 1
if (sp3 > 60000 and sp3 < 65000):
    matrizBolinha[2][2] = 1

imgStack = stackImages(0.5,([space7,space8,space9],[space4,space5,space6],[space1,space2,space3]))
imgStackc = stackImages(0.5,([spacec7,spacec8,spacec9],[spacec4,spacec5,spacec6],[spacec1,spacec2,spacec3]))

imgGeral = stackImages(0.5,[imgStack,imgStackc,captura,capturaBlur])
cv2.imshow("Tic Tac Toe",imgGeral)

print(matrizx)
print(matrizBolinha)
cv2.waitKey(0)
