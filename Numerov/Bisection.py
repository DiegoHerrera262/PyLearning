# Program for applying bisection for finding roots of function
# Author: Diego Alejandro Herrera Rojas
# Date: 25 - 04 - 20
# Description: This program aims to finding roots of a function using bisection
#              algorithm. It will be used for testing in order to include an
#              appropriate piece of code in Schrodinger.py
import numpy as np

TOP_ITER = 100
tol = 1e-7

def Bisection(myfunc, interval):
    xinf = interval[0]
    xsup = interval[1]
    xr = 0
    for i in range(0,TOP_ITER):
        yinf = myfunc(xinf)
        ysup = myfunc(xsup)
        if ysup * yinf < 0:
            xr = 0.5*(xinf + xsup)
            yr = myfunc(xr)
            if np.abs(yr) <= tol:
                return xr
            else:
                if yr * ysup > 0:
                    xsup = xr
                elif yr * yinf > 0:
                    xinf = xr
                else:
                    print('Fatal Problem')
                    return 'Error -1'
        elif yinf * yinf > 0:
            print('Bad selection of intervals')
            return 'Error 0'
        else:
            print('Fatal error')
            return 'Error 1'

class FunctionObject:

    def __init__(self,fun):
        self.funct = fun

# def func(x):
#    return x**2-2

# test = FunctionObject(func)
# print(Bisection(test.funct,[1.0,2.0]))
