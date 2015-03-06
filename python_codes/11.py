import numpy as np
import sympy
from sympy.abc import t
from sympy import Function, Derivative, dsolve, Eq
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


def numericalApproxForTwo(R, F, fR, fF, R0, F0, dt = 0.0005, steps = 300):
    def reduceSize(Range, p):
        return [Range[i] for i in range(len(Range)) if i%p == 0]

    tdomain = np.array([i*dt for i in range(steps)])

    Frange = [F0]
    Rrange = [R0]

    for t in tdomain[1:]:
        dR = fR.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
        dF = fF.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
        Rrange.append(Rrange[-1]+dt*dR)
        Frange.append(Frange[-1]+dt*dF)

    Trange = reduceSize(tdomain, 100)
    Rrange = reduceSize(Rrange, 100)
    Frange = reduceSize(Frange, 100)

    return Trange, Rrange, Frange

R = Function('R')
F = Function('F')

formulaR = F(t)
formulaF = -4*R(t)

Tvals,Rvals,Fvals = numericalApproxForTwo(R, F, formulaR, formulaF, 1.0, 1.0, dt = 0.0005, steps = 12500)

# component graph!
plt.plot(Tvals,Rvals, 'lightblue',Tvals,Fvals, 'darkblue')

# solution curve in phase plane
plt.plot(Rvals, Fvals)
