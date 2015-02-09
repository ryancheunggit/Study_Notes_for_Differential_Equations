# three point slopes

# library
import matplotlib.pyplot as plt
from sympy.abc import t
import numpy as np

# define the function
y = 1.0/(t**2+1.0/2)

# sample domain
domain = np.linspace(-3,3,30)

# calculate 3 slopes at tabled position
T = np.array([-1,0,1])
Y = np.array([2.0/3,2,2.0/3])
U = 1
V = -2*T*Y**2
N = np.sqrt(U**2+V**2)
U2, V2 = U/N, V/N

# make the plot
plt.plot(domain, [y.subs(t, tval) for tval in domain])
plt.quiver( T,Y,U2, V2)
plt.xlim([-3,3])
plt.ylim([0,3])

# the slope field
T,Y = np.meshgrid(domain,np.linspace(0,4,30) )
U = 1
V = -2*T*Y**2
N = np.sqrt(U**2+V**2)
U2, V2 = U/N, V/N

plt.quiver( T,Y,U2, V2)
plt.plot(domain,np.array([y.subs(t, tval) for tval in domain]), linewidth= 2)
plt.xlim([-3,3])
plt.ylim([0,4])
plt.xlabel(r"$t$")
plt.ylabel(r"$y$")

# part 2


def plotSlopeField(tdomain,ydomain,formula,points = []):
    # initialize figure
    fig = plt.figure(num=1)

    # create grid
    T,Y = np.meshgrid(tdomain,ydomain )

    # calculate slope vectors
    U = 1
    V = np.array([[formula.subs({y(t): yval, t: tval}) for tval in tdomain] for yval in ydomain],dtype = 'float')
    N = np.sqrt(U**2+V**2)
    U2, V2 = U/N, V/N

    # make the plot
    plt.quiver( T,Y,U2, V2)
    plt.xlabel(r"$t$")
    plt.ylabel(r"$y$")
    plt.axhline(0,0,1,linewidth = 2, color = 'black')
    plt.axvline(0,0,1,linewidth = 2, color = 'black')

    # solve the differential equation
    from sympy import Derivative, dsolve
    solutions = dsolve(Derivative(y(t),t)-formula,y(t)).args[1]

    # plot the solutions through the given points
    if points != []:
        for p in points:
            from sympy import Eq, solve
            C1 = solve(Eq(solutions.subs(t,p[0]),p[1]))[0]
            solution = solutions.subs('C1',C1)
            plt.plot(tdomain, np.array([solution.subs(t,tval) for tval in tdomain],dtype= 'float'),
                    linewidth = '2')

        # limiting the axes
        plt.xlim([tdomain[0],tdomain[-1]])
        plt.ylim([ydomain[0],ydomain[-1]])



    return fig

domain = np.linspace(-3,3,30)
from sympy.abc import t
from sympy import Function
y = Function('y')
formula = y(t) - t

fg = plotSlopeField(domain,domain,formula,[(2,4),(1,3),(0,2),(2,0),(2,1),(1,1),(0,0)])
fg.show()


# practice
formula2 = 0.2*(t - 1)**2 + 0.5*y(t)
domain2 = np.linspace(-5,5,30)
fg2 = plotSlopeField(domain2,domain2,formula2,[(5,5)])
fg2.show()


# special case
import sympy
formula3 = sympy.cos(t)
tdomain3 = np.linspace(-6,6,30)
ydomain3 = np.linspace(-2,2,30)
fg3 = plotSlopeField(tdomain3,ydomain3,formula3,[(0,0),(0,1),(0,-1)])
fg3.show()

# exercise
formula4 = t*(t**2-1)
tdomain = np.linspace(-2,2,30)
ydomain = np.linspace(-1,1,30)
fg4 = plotSlopeField(tdomain3,ydomain3,formula3)
fg4.show()
