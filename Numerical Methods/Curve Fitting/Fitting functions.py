import math
import matplotlib.pyplot as plt
import random


def linearFit(x, y):
    '''
    Uses least squares method to perform a linear fit on the data
    '''
    n = len(x)
    X = 0
    Y = 0
    XY = 0
    X2 = 0
    Y2 = 0
    for i in range(len(x)):
        X += x[i]
        Y += y[i]
        XY += x[i]*y[i]
        X2 += x[i]**2
        Y2 += y[i]**2

    a = (n*XY-X*Y)/(n*X2-X**2)
    b = Y/n-a*X/n
    return a, b

# def polynomialFit(x, y, m=2):
#     a = (m+1)*[0]
#     return a


def powerLawFit(x, y):
    '''
    returns α and β respectively in the equation 
    y= β*α^x
    '''
    lny = [math.log(yi) for yi in y]
    a, b = linearFit(x, lny)

    return math.e**a, math.e**b

# x=list(range(1,11))
# y=[3*4**xi+(-1+2*random.random()) for xi in x]
# print(powerLawFit(x,y))


def exponentialFit(x, y):
    '''
    returns α and β respectively in the equation 
    y= βe^(αx)
    '''
    lny = [math.log(yi) for yi in y]
    a, b = linearFit(x, lny)

    return a, math.e**b

# x=list(range(1,11))
# y=[3*math.exp(4*xi)+(-1+2*random.random()) for xi in x]
# print(exponentialFit(x,y))


def saturationFit(x, y):
    '''
    returns α and β respectively in the equation 
         α x
    y= -------
        x + β
    '''
    invx = [1/xi for xi in x]
    invy = [1/yi for yi in y]
    b, a = linearFit(invx, invy)

    return 1/a, b/a


# x = list(range(1, 11))
# y = [3*xi/(xi+4) for xi in x]
# print(saturationFit(x, y))
print('hello')
