import numpy as np
import sympy
from sympy.abc import t
from sympy import Function, Derivative, dsolve, Eq
import matplotlib.pyplot as plt

x = Function('x')
y = Function('y')
formulax = y(t)
formulay = -4*x(t)
eq = [Eq(Derivative(x(t),t),formulax), Eq(Derivative(y(t),t),formulay)]
dsolve(eq)

def eulerSystem(Y, y0, variables, dt, steps):
    tdomain = np.array([i*dt for i in range(steps)])
    for t in tdomain[1:]:
        d = [f.subs({variables[i]:y0[i][-1] for i in range(len(variables))}) for f in Y]
        for i in range(len(y0)):
            y0[i].append(y0[i][-1] + d[i]*dt)
    return y0


Y = [formulax, formulay]
y0 = [[1],[0]]
y1 = [[0],[2]]
variables = ['x(t)', 'y(t)']
values0 = eulerSystem(Y, y0, variables, dt = 0.001, steps  =4000)
values1 = eulerSystem(Y, y1, variables, dt = 0.001, steps  =4000)
plt.plot(values0[0], values0[1], 'blue')
plt.plot(values1[0], values1[1], 'red')


x = Function('x')
y = Function('y')
formulax = -1*x(t)+y(t)
formulay = -1*y(t)
eq = [Eq(Derivative(x(t),t),formulax), Eq(Derivative(y(t),t),formulay)]
dsolve(eq)

Y = [formulax, formulay]
y0 = [[-1],[0]]
values0 = eulerSystem(Y, y0, variables, dt = 0.001, steps  =4000)
plt.plot(values0[0], values0[1], 'blue')



x = Function('x')
y = Function('y')
from sympy.abc import t

formulax = x(t)**2+y(t)
formulay = x(t)**2*y(t)**2
eq = [Eq(Derivative(x(t),t),formulax), Eq(Derivative(y(t),t),formulay)]
dsolve(eq)


