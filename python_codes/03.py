# module 3 Separation of Variables
# part 1 Method of Substitution
import sympy
from sympy.abc import t
print sympy.integrate(sympy.cos(t**2),t)

print sympy.integrate(sympy.cos(t**2)*2*t,t)

# ex1
from sympy.abc import x
print sympy.integrate((4*x)/(1+4*x**2),x)

# part 2 separable equations
from sympy.abc import y
f = -2*t*y**2
print sympy.separatevars(f, symbols=(t,y))

print sympy.separatevars(y**3+t**2, symbols=(t,y))


# ex2
print sympy.separatevars(t*y+t*y**2, symbols=(t,y))


print sympy.separatevars(t**2*y+t*y**2, symbols=(t,y))

# ex3



# ex4
from sympy import Function, dsolve, Derivative
y = Function('y')
dsolve(Derivative(y(t),t)-2*t*(y(t))**2-3*(y(t))**2,y(t))

# newton

T = Function('T')
from sympy.abc import c, a
dsolve(Derivative(T(t),t)-a*(T(t)-c),T(t))
