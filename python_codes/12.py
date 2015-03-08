import numpy as np
import sympy
from sympy.abc import t
from sympy import Function, Derivative, dsolve, Eq
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


def numericalApproxForTwo(fR, fF, R0, F0, dt = 0.0005, steps = 300):
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
    
def directionField(fR, fF, Rdomain, Fdomain):
    fig = plt.figure(num=1)
    Rvals,Fvals = np.meshgrid(Rdomain,Fdomain)
    r = np.array([[fR.subs({'R(t)':rval, 'F(t)':fval}) for rval in Rdomain] for fval in Fdomain],dtype = 'float')
    f = np.array([[fF.subs({'R(t)':rval, 'F(t)':fval}) for rval in Rdomain] for fval in Fdomain],dtype = 'float')
    n = np.sqrt(r**2+f**2)
    r, f = r/n, f/n
    plt.quiver(Rvals, Fvals, r, f)
    plt.xlabel(r"$R$")
    plt.ylabel(r"$F$")
    plt.axhline(0,0,1,linewidth = 2, color = 'black')
    plt.axvline(0,0,1,linewidth = 2, color = 'black')
    return fig
    
R = Function('R')
F = Function('F')

formulaR = F(t)
formulaF = -3*R(t)

Rdomain = np.linspace(-6,6,30)
Fdomain = np.linspace(-6,6,30)

fg1 = directionField(formulaR, formulaF,Rdomain, Fdomain)
Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, 3.0, 0.0, dt = 0.0005, steps = 20000)
plt.plot(Rvals, Fvals)
fg1.show()

R = Function('R')
F = Function('F')

formulaR = F(t)
formulaF = -3*R(t) - 0.1*F(t)

Rdomain = np.linspace(-6,6,30)
Fdomain = np.linspace(-6,6,30)

fg2 = directionField(formulaR, formulaF,Rdomain, Fdomain)
Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, 3.0, 0.0, dt = 0.0005, steps = 20000)
plt.plot(Rvals, Fvals)
fg2.show()


R = Function('R')
F = Function('F')

formulaR = F(t)
formulaF = -3*R(t) - 0.5*F(t)

Rdomain = np.linspace(-6,6,30)
Fdomain = np.linspace(-6,6,30)

fg3 = directionField(formulaR, formulaF,Rdomain, Fdomain)
Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, 3.0, 0.0, dt = 0.0005, steps = 20000)
plt.plot(Rvals, Fvals)
fg3.show()


### ex 2

R = Function('R')
F = Function('F')

formulaR = F(t)
formulaF = -3*R(t) - 4*F(t)

Rdomain = np.linspace(-5,5,30)
Fdomain = np.linspace(-5,5,30)

points = [(1,-1),(1,-3),(1,1)]

fg4 = directionField(formulaR, formulaF,Rdomain, Fdomain)
for point in points:
    Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, point[0], point[1], dt = 0.0005, steps = 20000)
    plt.plot(Rvals, Fvals, linewidth = 3)
fg4.show()

