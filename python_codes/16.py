import numpy as np
import sympy
from sympy.abc import t
from sympy import Function, Derivative, dsolve, Eq
import matplotlib.pyplot as plt

S = Function('S')
II = Function('II')
formulaS = -0.00218*S(t)*II(t)
formulaI = 0.00218*S(t)*II(t)-0.44036*II(t)
eq = [Eq(Derivative(S(t),t),formulaS), Eq(Derivative(II(t),t),formulaI)]

def eulerSystem(Y, y0, variables, dt, steps):
    tdomain = np.array([i*dt for i in range(steps)])
    for t in tdomain[1:]:
        d = [f.subs({variables[i]:y0[i][-1] for i in range(len(variables))}) for f in Y]
        for i in range(len(y0)):
            y0[i].append(y0[i][-1] + d[i]*dt)
    return y0

Y = [formulaS, formulaI]
y0 = [[762],[1]]
variables = ['S(t)', 'II(t)']
values = eulerSystem(Y, y0, variables, dt = 0.001, steps  =4000)
t = [0.001*(i+1) for i in range(len(values[0]))]
plt.plot(t,values[0],'blue', t, values[1], 'red')