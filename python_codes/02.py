from sympy.abc import t
import sympy
from sympy import E as E
sympy.diff(1/(t**2+1),t)

# ex
y = 3*E**(2*t)-1.0/2
sympy.diff(y,t) == 2*y+1

y = sympy.log(t+3)
sympy.diff(y,t) == E**(-1*y)

y = 4*E**(3*t)+E**(7*t)
sympy.diff(y,t) == 3*y+E**(7*t)

# ex
from sympy import Function, dsolve, Derivative

w = Function('w')
dsolve(Derivative(w(t),t)-w(t),w(t))

y = Function('y')
dsolve(Derivative(y(t),t)-(y(t))**3-t**2,y(t))

sympy.diff(1.0/(2*t-1),t)

# Bob
y= t
sympy.diff(y,t) == (y+1)/(t+1)

# Glen
y = 2*t+1
sympy.diff(y,t) == (y+1)/(t+1)

y = t**2-2
sympy.diff(y,t) == (y+1)/(t+1)

y = Function('y')
dsolve(Derivative(y(t),t)-(y(t)+1)/(t+1),y(t))
