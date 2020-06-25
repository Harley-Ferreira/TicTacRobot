from numpy import arccos, arctan2
from math import pow, degrees, sqrt


def conversor(x, y, l1, l2):

    #Teta 2
    n = pow(x, 2) + pow(y, 2) - pow(l1, 2) - pow(l2, 2)
    d = 2 * l1 * l2
    teta2 = degrees(arccos(n/d))

    #Teta 1
    alfa = arctan2(y, x)
    r = sqrt(pow(x, 2) + pow(y, 2))
    n = pow(l2, 2) - pow(l1, 2) - pow(r, 2)
    d = -2 * l1 * r
    beta = arccos(n/d)
    teta1 = degrees(alfa - beta)

    #print(f'Teta 1: {teta1}    Teta 2: {teta2}')

    return(teta1, teta2)


# x = conversor(-150,150,150,150)
# print(f" {x[0]}   {x[1]}")
