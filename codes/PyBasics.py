# Program to show Python basics

# Date: 23-12-19
# AUthor: Diego Herrera
# Description: This program implements a recursive bisection algorithm to find
#              square root of real positive number.

import math as mt

def bisection(num, guess_inf, guess_sup):
    fi = guess_inf**2 - num
    fs = guess_sup**2 - num
    # Definition of root by bisection
    root = 0.5*(guess_inf + guess_sup)
    fr = root**2 - num
    # Condition to finish (inner stack)
    if mt.fabs(fr) < 1e-5:
        print("I found: ", root)
    # Recursive call
    else:
        print("Still in: ", root)
        if fi*fr > 0:
            bisection(num, root, guess_sup)
        elif fs*fr > 0:
            bisection(num, guess_inf, root)
        else:
            print("bad luck")

# Main program execution
    
num = input("I'll find square root of: ")         # Input captures a string
num = float(num)                                  # Convert to integer type
seed_inf = input("with inf. seed: ")              # Input captures a string
seed_inf = float(seed_inf)
seed_sup = input("with sup. seed: ")              # Input captures a string
seed_sup = float(seed_sup)

bisection(num,seed_inf,seed_sup)                  # Uses sure seeds
