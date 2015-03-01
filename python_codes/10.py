# systems of differential equations
# notice solving systems of differential equations in sympy require the
# sympy version 0.7.6

import sympy
from sympy.abc import t, a, C
from sympy import Function, Derivative, dsolve, Eq, solve

y1= Function('y1')
y2= Function('y2')
eqs=[Eq(y1(t).diff(t),y1(t)+2*y2(t)),
     Eq(y2(t).diff(t),-2*y1(t)+y2(t)+2*sympy.exp(t))]
s= dsolve(eqs)

print s
