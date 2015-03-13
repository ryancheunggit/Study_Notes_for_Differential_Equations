import numpy as np
import sympy
from sympy.abc import t
from sympy import Function, Derivative, dsolve, Eq
import matplotlib.pyplot as plt
    
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

formulaR = 2*F(t) - R(t)
formulaF = R(t)

Rdomain = np.linspace(-1,10,30)
Fdomain = np.linspace(-1,10,30)

fg1 = directionField(formulaR, formulaF,Rdomain, Fdomain)
tdomain = np.linspace(-2.2,2.2,30)
Rvals = [exp(t) + exp(-1*t) for t in tdomain]
Fvals = [exp(t) for t in tdomain]
plt.plot(Rvals, Fvals, linewidth = 2)
fg1.show()

fg2 = plt.figure()
plt.plot(tdomain, Rvals, 'r', tdomain, Fvals, 'b')

# solve using dsolve?

x = Function('x')
y = Function('y')
from sympy.abc import t
eqs=[Eq(x(t).diff(t),2*x(t)+3*y(t)),
     Eq(y(t).diff(t),-4*y(t))]
s= dsolve(eqs)

print s

