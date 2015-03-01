# systems of differential equations
# notice solving systems of differential equations in sympy require the
# sympy version 0.7.6
import numpy as np
import sympy
from sympy.abc import t, a, C
from sympy import Function, Derivative, dsolve, Eq, solve
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D


y1= Function('y1')
y2= Function('y2')
eqs=[Eq(y1(t).diff(t),y1(t)+2*y2(t)),
     Eq(y2(t).diff(t),-2*y1(t)+y2(t)+2*sympy.exp(t))]
s= dsolve(eqs)



# fox and rabbit example

R = Function('R')
F = Function('F')

formulaR = 2*R(t) - 1.2*R(t)*F(t)
formulaF = -1*F(t) + 0.9*R(t)*F(t)

eqs = [Eq(Derivative(R(t),t), formulaR),
       Eq(Derivative(F(t),t), formulaF)]

# try numerical method

tdomain = np.array([i*0.0005 for i in range(32000)])
dt = 0.0005

Rrange = [1.0]
Frange = [0.5]

# for faster plotting
def reduceSize(Range, p):
    return [Range[i] for i in range(len(Range)) if i%p == 0]

# numerical approxmation SLOW!
for t in tdomain[1:]:
    dR = formulaR.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
    dF = formulaF.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
    Rrange.append(Rrange[-1]+dt*dR)
    Frange.append(Frange[-1]+dt*dF)

Trange = reduceSize(tdomain, 100)
Rrange = reduceSize(Rrange, 100)
Frange = reduceSize(Frange, 100)

# component graph!
plt.plot(Trange,Rrange, 'lightblue',Trange,Frange, 'darkblue')

# solution curve in phase plane
plt.plot(Rrange, Frange)

Rrange2 = [1.0]
Frange2 = [0.25]
for t in tdomain[1:]:
    dR = formulaR.subs({'R(t)':Rrange2[-1] , 'F(t)': Frange2[-1]})
    dF = formulaF.subs({'R(t)':Rrange2[-1] , 'F(t)': Frange2[-1]})
    Rrange2.append(Rrange2[-1]+dt*dR)
    Frange2.append(Frange2[-1]+dt*dF)

Rrange2 = reduceSize(Rrange2, 100)
Frange2 = reduceSize(Frange2, 100)

Rrange3 = [10.0/9]
Frange3 = [5.0/3]

# phase portrait
plt.plot(Rrange, Frange, 'blue', Rrange2, Frange2, 'blue', Rrange3, Frange3, 'bo')


# 3D plot!
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(Rrange, Frange, Trange)
ax.plot(Rrange, Frange, [0 for t in Trange])
ax.plot([0 for t in Trange], Frange, Trange)
ax.plot(Rrange, [0 for t in Trange], Trange)
ax.set_xlabel(r'$R(t)$')
ax.set_ylabel(r'$F(t)$')
ax.set_zlabel(r'$t$')
plt.show()


# exercise 4

R = Function('R')
F = Function('F')

formulaR = 2*(1-R(t)/3.0)*R(t) - R(t)*F(t)
formulaF = -2*F(t) + 4*R(t)*F(t)

Rrange = [1.0]
Frange = [0.5]

tdomain = np.array([i*0.01 for i in range(32000)])
dt = 0.0005

for t in tdomain[1:]:
    dR = formulaR.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
    dF = formulaF.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
    Rrange.append(Rrange[-1]+dt*dR)
    Frange.append(Frange[-1]+dt*dF)

Trange = reduceSize(tdomain, 100)
Rrange = reduceSize(Rrange, 100)
Frange = reduceSize(Frange, 100)

# component graph!
plt.plot(Trange,Rrange, 'lightblue',Trange,Frange, 'darkblue')

# solution curve in phase plane
plt.plot(Rrange, Frange)


# ex 5

y = Function('y')
v = Function('v')

formulay = v(t)
formulav = -2*y(t)

yrange = [2.0]
vrange = [0.45]

tdomain = np.array([i*0.0005 for i in range(32000)])
dt = 0.0005

for t in tdomain[1:]:
    dy = formulay.subs({'v(t)':vrange[-1]})
    dv = formulav.subs({'y(t)':yrange[-1]})
    yrange.append(yrange[-1]+dt*dy)
    vrange.append(vrange[-1]+dt*dv)

Trange = reduceSize(tdomain, 100)
yrange = reduceSize(yrange, 100)
vrange = reduceSize(vrange, 100)

# component graph!
plt.plot(Trange,yrange, 'lightblue',Trange,vrange, 'darkblue')

# solution curve in phase plane
plt.plot(yrange, vrange)


# ps

R = Function('R')
F = Function('F')

formulaR = 2*(1-R(t)/3.0)*R(t) - R(t)*F(t)
formulaF = -16*F(t) + 4*R(t)*F(t)

Rrange = [8.0]
Frange = [1.0]

tdomain = np.array([i*0.01 for i in range(32000)])
dt = 0.0005

for t in tdomain[1:]:
    dR = formulaR.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
    dF = formulaF.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
    Rrange.append(Rrange[-1]+dt*dR)
    Frange.append(Frange[-1]+dt*dF)

Trange = reduceSize(tdomain, 100)
Rrange = reduceSize(Rrange, 100)
Frange = reduceSize(Frange, 100)

# component graph!
plt.plot(Trange,Rrange, 'lightblue',Trange,Frange, 'darkblue')

# solution curve in phase plane
plt.plot(Rrange, Frange)
