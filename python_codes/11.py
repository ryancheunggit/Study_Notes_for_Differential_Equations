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

R = Function('R')
F = Function('F')

formulaR = F(t)
formulaF = -1*R(t)

Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, 1.0, 1.0, dt = 0.0005, steps = 20000)

# component graph!
plt.plot(Tvals,Rvals, 'lightblue',Tvals,Fvals, 'darkblue')

# solution curve in phase plane
plt.plot(Rvals, Fvals)

# direction Field

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
formulaF = -1*R(t)

Rdomain = np.linspace(-3,3,30)
Fdomain = np.linspace(-3,3,30)

fg1 = directionField(formulaR, formulaF,Rdomain, Fdomain)
fg1.show()

# vector field

def vectorField(fR, fF, Rdomain, Fdomain, points = [], steps = 5):
    fig = plt.figure(num=1)
    colors = ['red', 'green', 'blue', 'orange', 'black']
    for i, point in enumerate(points):
        Rvals, Fvals, r,f = [], [], [], []
        pr, pf = point[0], point[1]
        for step in range(steps):
            Rvals.append(pr)
            Fvals.append(pf)
            r.append(int(fR.subs({'R(t)': Rvals[-1], 'F(t)':Fvals[-1]})))
            f.append(int(fF.subs({'R(t)': Rvals[-1], 'F(t)':Fvals[-1]})))
            pr, pf = pr+r[-1], pf+f[-1]
            plt.arrow(Rvals[-1],Fvals[-1],r[-1],f[-1], head_width = 0.2)
    plt.xlim([Rdomain[0],Rdomain[-1]])
    plt.ylim([Fdomain[0],Fdomain[-1]])
    return fig

R = Function('R')
F = Function('F')

formulaR = F(t)
formulaF = -1*R(t)

Rdomain = np.linspace(-9,9,30)
Fdomain = np.linspace(-9,9,30)

fg2 = vectorField(formulaR, formulaF, Rdomain, Fdomain, points = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)], steps = 5)


#

R = Function('R')
F = Function('F')

formulaR = -1*F(t)
formulaF = R(t)-0.3*F(t)

Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, 0, 1.5, dt = 0.0005, steps = 25000)

# component graph!
plt.plot(Tvals,Rvals, 'lightblue',Tvals,Fvals, 'darkblue')

Rdomain = np.linspace(-2,2,30)
Fdomain = np.linspace(-2,2,30)

fg3 = directionField(formulaR, formulaF,Rdomain, Fdomain)
plt.plot(Rvals, Fvals)

fg3.show()


# ex2

R = Function('R')
F = Function('F')

formulaR = F(t)
formulaF = 3*R(t) - R(t)**3 -2*F(t)

Rdomain = np.linspace(-4,4,30)
Fdomain = np.linspace(-5,5,30)

fg4 = directionField(formulaR, formulaF,Rdomain, Fdomain)

# ex
R = Function('R')
F = Function('F')

formulaR = 2*R(t)*(1- R(t)/2.0) - F(t)*R(t)
formulaF = 3*F(t)*(1- F(t)/3.0) - 2*R(t)*F(t)

Rdomain = np.linspace(0,4,30)
Fdomain = np.linspace(0,4,30)

fg5 = directionField(formulaR, formulaF,Rdomain, Fdomain)
points = [(0.3,0.2),(0.5,0.2),(2.0,4.0),(4.0,2.0),(3,4),(4,3),(0.3,0.4),(0.2,0.2)]
for point in points:
    Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, point[0], point[1], dt = 0.001, steps = 20000)
    plt.plot(Rvals, Fvals)

fg5.show()


# exercise 1
R = Function('R')
F = Function('F')

formulaR = R(t) + 2*F(t)
formulaF = -1*F(t)

Rdomain = np.linspace(-5,5,30)
Fdomain = np.linspace(-5,5,30)

fg6 = directionField(formulaR, formulaF,Rdomain, Fdomain)
points = [(-2,2)]
for point in points:
    Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, point[0], point[1], dt = 0.001, steps = 20000)
    plt.plot(Rvals, Fvals)

fg6.show()

