# Program for integrating dicrete function using Trapezoid
# Author: Diego Alejandro Herrera Rojas
# Date: 25 - 04 - 20
# Description: This program aims to integrating wavefunction using Trapezoid
#              rule it will be used for testing in order to include an
#              appropriate piece of code in Schrodinger.py

import numpy as np

def Trapezoid(samplesfunc,dr):
    top = len(samplesfunc)-1
    norm = 0
    for i in range(0,top):
        norm = norm + 0.5*dr*(samplesfunc[i] + samplesfunc[i+1])
    return norm

# N = 1000
# dt = np.pi/N
# t = (np.pi/N)*np.array(range(0,N+1))

# f = np.sin(t)
# print(Trapezoid(f,dt))
