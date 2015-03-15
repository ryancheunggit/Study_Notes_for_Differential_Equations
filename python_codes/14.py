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
    
    
    
R = Function('R')
F = Function('F')

formulaR = F(t)
formulaF = -2*R(t) - 3*F(t)

Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, 1.0, 1.0, dt = 0.25, steps = 7)


for i in range(len(Rvals)):
    print "%10s" % Rvals[i], "%10s" % Fvals[i]
    
    
def eulerSystem(Y, y0, variables, dt, steps):
    tdomain = np.array([i*dt for i in range(steps)])
    for t in tdomain[1:]:
        d = [f.subs({variables[i]:y0[i][-1] for i in range(len(variables))}) for f in Y]
        for i in range(len(y0)):
            y0[i].append(y0[i][-1] + d[i]*dt)
    return y0
            
x = Function('x')
y = Function('y')
formulax = y(t)
formulay = -2*x(t) - 3*y(t)
Y = [formulax, formulay]
y0 = [[1],[1]]
variables = ['x(t)', 'y(t)']

values = eulerSystem(Y, y0, variables, dt = 0.25, steps  =5)
for i in range(len(values[0])):
    print "%10s" % values[0][i], "%10s" % values[1][i]
    

# ex1
x = Function('x')
y = Function('y')
formulax = y(t)
formulay = -sympy.sin(x(t))
Y = [formulax, formulay]
y0 = [[0],[2]]
variables = ['x(t)', 'y(t)']

values = eulerSystem(Y, y0, variables, dt = 0.25, steps  =9)
for i in range(len(values[0])):
    print "%10s" % values[0][i], "%10s" % values[1][i]

#ex2
x = Function('x')
y = Function('y')
formulax = y(t) + (y(t))**2
formulay = -x(t)+y(t)/5.0-x(t)*y(t)+1.2*(y(t))**2
Y = [formulax, formulay]
y0 = [[1],[1]]
variables = ['x(t)', 'y(t)']

values = eulerSystem(Y, y0, variables, dt = 0.25, steps  =9)
for i in range(len(values[0])):
    print "%10s" % values[0][i], "%10s" % values[1][i]
    
#ex3
x = Function('x')
y = Function('y')
formulax = 2*x(t)
formulay = y(t)
Y = [formulax, formulay]
y0 = [[1],[3]]
variables = ['x(t)', 'y(t)']

values = eulerSystem(Y, y0, variables, dt = 0.5, steps  =13)
for i in range(len(values[0])):
    print "%10s" % values[0][i], "%10s" % values[1][i]

tvals = [4,8,12]
for tv in tvals:
    print ((values[0][tv]-exp(2*tv*0.5))**2 + (values[1][tv]-3*exp(tv*0.5))**2)**0.5
    
    
x = Function('x')
y = Function('y')
formulax = 2*x(t)
formulay = y(t)
Y = [formulax, formulay]
y0 = [[1],[3]]
variables = ['x(t)', 'y(t)']

values = eulerSystem(Y, y0, variables, dt = 0.1, steps  =61)
for i in range(len(values[0])):
    print "%10s" % values[0][i], "%10s" % values[1][i]

tvals = [20,40,60]
for tv in tvals:
    print ((values[0][tv]-exp(2*tv*0.1))**2 + (values[1][tv]-3*exp(tv*0.1))**2)**0.5
    
    
# ex4 
y = Function('y')
v = Function('v')
formulay = v(t)
formulav = -0.5*v(t) - 2*y(t)
Y = [formulay, formulav]
y0 = [[2],[0]]
variables = ['y(t)', 'v(t)']
values = eulerSystem(Y, y0, variables, dt = 0.25, steps  =41)
plt.plot(y0[0], y0[1])

values = eulerSystem(Y, y0, variables, dt = 0.1, steps  =11)
plt.plot(y0[0], y0[1])