import numpy as np
import sympy
from sympy.abc import t
from sympy import Function, Derivative, dsolve, Eq
import matplotlib.pyplot as plt

def numericalApproxForTwo(fR, fF, R0, F0, dt = 0.0005, steps = 300):
    tdomain = np.array([i*dt for i in range(steps)])

    Frange = [F0]
    Rrange = [R0]

    for t in tdomain[1:]:
        dR = fR.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
        dF = fF.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
        Rrange.append(Rrange[-1]+dt*dR)
        Frange.append(Frange[-1]+dt*dF)

    return tdomain, Rrange, Frange

R = Function('R')
F = Function('F')

formulaR = -1*F(t)
formulaF = R(t) -1*F(t)

Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, 2.0, 0.0, dt = 0.5, steps = 20)


for i in range(4):
    print "%10s" % Rvals[i], "%10s" % Fvals[i]