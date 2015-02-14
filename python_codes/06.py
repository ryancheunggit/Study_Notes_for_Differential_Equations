# existance theorem
import sympy

from sympy.abc import t
from sympy import Function, Derivative, dsolve, Eq, solve
y = Function('y')

formula = 1+y(t)**2

solutions = dsolve(Eq(Derivative(y(t),t),formula))

print solutions

solution = solutions.args[1].subs('C1',solve(Eq(solutions.args[1].subs(t,0),0))[0])


#  uniqueness of solution

tdomain = np.linspace(-7,7,30)

formula = sympy.root(y(t),3)*sympy.sin(2*t)

solution1 = 0
solution2 = (8.0/27)**0.5*(sympy.sin(t))**3
solution3 = -1*(8.0/27)**0.5*(sympy.sin(t))**3

plt.plot(tdomain, [0 for i in tdomain], 'blue', \
         tdomain, np.array([solution2.subs(t, tval) for tval in tdomain]), 'black',\
         tdomain, np.array([solution3.subs(t, tval) for tval in tdomain]), 'red')


# ps 1

# ps 2

formula = 1.0/(y(t)+2)**2
dsolve(Eq(Derivative(y(t),t),formula))

# ps 3
formula = sympy.root(y(t),3)*sympy.sin(2*t)
dsolve(Eq(Derivative(y(t),t),formula))

# ps 4

formula = -1*y(t)**2+y(t)+2*y(t)+t**2+2*t-t**2-t**4
dsolve(Eq(Derivative(y(t),t),formula))

formula.subs('y(t)', t**2-1).simplify()

formula.subs('y(t)', t**2).simplify()

formula.subs('y(t)', t**2+1).simplify()

formula.subs('y(t)', t**2+2).simplify()

# ps 5

formula = y(t)/(t**2)
dsolve(Eq(Derivative(y(t),t),formula))
