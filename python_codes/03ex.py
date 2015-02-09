import sympy
from sympy import Function, dsolve, Derivative
from sympy.abc import t

y = Function('y')

dsolve(Derivative(y(t),t)-y(t)+y(t)**2,y(t))


dsolve(Derivative(y(t),t)-t**2*y(t)**3,y(t))

f = -1*sympy.sqrt((-6)/(-6+4*t**3))
f.diff()

# CARBON MONOXIDE

c = Function('c')

eq = 1 - c(t)/10

dsolve(Derivative(c(t),t)-eq,c(t))

# sky diver
from sympy.abc import v, t, m, g, k, c
v = Function('v')
eq = g - k/m*v(t)**2
dsolve(Derivative(v(t),t)-eq,v(t))
