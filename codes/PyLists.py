# Program to demonstrate lists

# Date: 24-12-19
# Author: Diego Herrera
# Description: This program implements a simple iteration
#              over a python list to compute an integral
#              using Simpson rule

import numpy as np

def simps_int(lim_inf, lim_sup, STEPS):
    # Parameters of integration
    l = lim_sup - lim_inf          # Lenght of interval
    dl = l/(2.0*STEPS)             # Steps of interval
    part = range(2*STEPS +1)       # List for partition
    # Auxiliary variables
    suma = 0.0                     # Partial sumation
    ii = 0                         # Counter
    x_aux = 0.0                    # Aux. variable 1
    fx = 0.0                       # AUx. variable 2
    print("Step interval is:", dl)
    # Computes partition and Simpson rule
    for x in part:
        x_aux = x * dl + lim_inf
        fx = np.sin(x_aux)         # EDIT FUNC. HERE
        # Discriminate inner and external points
        if ii%2 == 0:
            if ii == 0 or ii == 2*STEPS:
                suma = suma + fx * dl/3.0
            else:
                suma = suma + 2.0 * fx * dl/3.0
            
        else:
            suma = suma + fx * 4.0*dl/3.0
        # print(ii, x, x_aux, suma)
        ii = ii + 1
    return suma

x_inf = input("Enter inferior limit: ")
x_inf = float(x_inf)
x_sup = input("Enter superior limit: ")
x_sup = float(x_sup)
STEPS = input("Enter num. steps: ")
STEPS = int(STEPS)

integral = simps_int(x_inf, x_sup, STEPS)
print("I computed the integral of my_func:",integral)
