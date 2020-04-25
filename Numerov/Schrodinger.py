# Program for numerically solving Schrodinger's equation
# Author: Diego Alejandro Herrera Rojas
# Date: 23 - 04 - 20
# Description: This program aims to determining both proton and neutron
#              energy levels in the context of the nucleon - nuclei interac-
#              tion as described by the shell model. The numerical algorithm
#              is numerov, combined with a trigger method.

import numpy as np
import matplotlib.pyplot as plt
from Bisection import Bisection         # Bisection as implemented by me
from Trapezoid import Trapezoid         # Integration implemented by me

V_0 = 50.0
a = 0.5
R = 1.25

#########################MODELING OF A 1D QUANTUM SYSTEM########################

class D1_Quantum_Syst:

    def __init__(self, mypot, xrange, dr):
        # Fundamental constants
        self.mu_hbar = 1.0
        # Parameters for integration
        self.tol = 1e-7
        self.top_iter = 100
        self.dE = 0.5
        # Parameters of system - discretization
        self.mypot = mypot
        self.xrange = xrange
        self.dr = dr
        if np.abs(self.xrange[0]) <= self.tol:
            self.xrange[0] = 1e-4

    def wave_num2(self, l, E, r):
        return self.mu_hbar*(E-self.mypot(r)) - l*(l+1)/r**2

    # Two directions of integration 'forward' & 'backwards'
    # In reverse, input [beforelast, last]
    def NumerovInteg(self, l, E, init_vals, direction):
        # Set up discretization of space
        deltar = self.xrange[1] - self.xrange[0]
        N = int(deltar/self.dr)
        r = self.dr*np.array(range(0,N+1))
        size = len(r)
        r = self.xrange[0]*np.ones(size) + r

        # Set up array for numerov integration
        psi = np.zeros(size)
        # phi of numerov formula
        phi = lambda l,E,y,t: t*(1.0 + (self.dr)**2/12.0 * \
                self.wave_num2(l,E,y))

        if direction == 'forward':
            # Initialize values for integration
            psi[0] = init_vals[0]; psi[1] = init_vals[1];
            # Forward integration using Numerov
            idx = 2
            while idx < size:
                # Numerov Formula
                q = 2*phi(l,E,r[idx-1],psi[idx-1])-phi(l,E,r[idx-2],psi[idx-2])\
                    - (self.dr)**2 * self.wave_num2(l,E,r[idx-1]) * psi[idx-1]
                # Recover psi
                psi[idx] = q/phi(l,E,r[idx],1.0)
                idx = idx + 1
            return [psi, r, E]
        elif direction == 'backwards':
            # Initialize values for integration
            psi[size-2] = init_vals[0]; psi[size-1] = init_vals[1];
            # Backward integration using Numerov
            idx = size - 3
            while idx >= 0:
                # Numerov Formula
                q = 2*phi(l,E,r[idx+1],psi[idx+1])-phi(l,E,r[idx+2],psi[idx+2])\
                    - (self.dr)**2 * self.wave_num2(l,E,r[idx+1]) * psi[idx+1]
                # Recover psi
                psi[idx] = q/phi(l,E,r[idx],1.0)
                idx = idx - 1
            return [psi, r, E]
        else:
            print('Not valid direction of integrator (Numerov)')
            return [psi, r, E]

    # Always input [inf_limit, upper_limit]
    # For setting up boundary conditions
    def delta(self, l, E, init_vals, direction, bound_conds):
        mydata = self.NumerovInteg(l,E,init_vals,direction)
        psi = mydata[0]
        size = len(psi)
        if direction == 'forward':
            got_bound = psi[size-1]
            return bound_conds[1] - got_bound
        elif direction == 'backwards':
            got_bound = psi[0]
            return bound_conds[0] - got_bound
        else:
            print('Not Valid Direction of Integration (Delta)')
            return -1

    # Always input [inf_limit, upper_limit]
    # Use bisection to set boundary conditions and energy
    def Integrate(self, l, Etest, init_vals, direction, bound_conds):
        # Auxiliar lambda for computing valid energy
        delta_func = lambda x : self.delta(l,x,init_vals,direction,\
                    bound_conds)
        # Finds Interval with change of sign
        Einf = Etest
        Esup = Etest
        Einterv = [0.0,0.0]
        for i in range(1,self.top_iter):
            Einf = Etest - i * self.dE
            Esup = Etest + i * self.dE
            if delta_func(Einf) * delta_func(Etest) < 0:
                Einterv = [Einf,Etest]
                break
            elif delta_func(Esup) * delta_func(Etest) < 0:
                Einterv = [Etest,Esup]
                break
        if np.linalg.norm(np.array(Einterv)) == 0.0:
            print('Not Found Energy')
            return 'Not Found Energy'
        else:
            # Finds energy that satisfies boundary conditions
            Efound = Bisection(delta_func,Einterv)
            return self.NumerovInteg(l,Efound,init_vals,direction)

    def PlotSolution(self, l, Etest, init_vals, direction, bound_conds):
        mydata = self.Integrate(l,Etest,init_vals,direction,bound_conds)
        if mydata == 'Not Found Energy':
            print('Try other seed for Energy')
            return 'Fatal Error'
        else:
            # Nomalization of wavefunction using trapezoid rulemydata[0]
            norm = Trapezoid(np.multiply(mydata[0],mydata[0]),self.dr)
            mydata[0] = (1.0/norm) * mydata[0]
            # Plotting wavefunction
            plt.xlabel('$r_{12}$ (fm)')
            plt.ylabel('$u(r_{12})$')
            plt.title('Numerical Solution using Numerov ($l =$'+str(l)+')')
            mylabel = '$E=$'+str(mydata[2])
            plt.plot(mydata[1],mydata[0],'',label=mylabel)
            plt.legend()

###########################POTENTIAL FOR INTEGRATION############################

def potential(r):
    return -V_0/(np.exp((r-R)/a)+1)

###########################MAIN BODY OF THE PROGRAM#############################

Nucleon = D1_Quantum_Syst(potential,[1e-4,5.2*R],0.01)
Nucleon.PlotSolution(0,-20.0,[7e-7,2e-7],'backwards',[1e-5,2e-5])
plt.show()
