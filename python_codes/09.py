import sympy
from sympy.abc import t, a, C
from sympy import Function, Derivative, dsolve, Eq, solve

# slope field

tdomain = np.linspace(-3,3,30)
ydomain = np.linspace(-5,5,30)

y = Function('y')
formula = -1*t*y(t)/(1+t**2)

fg = plotSlopeField(tdomain,ydomain,formula,[(0,4),(0,3),(0,2),(0,1),(0,-1),(0,-2),(0,-3),(0,-4)])

fg.show()


formula = -1*t*y(t)/(1+t**2) + (2*t**2+1)/(4*t**2+4)

solution = t/4+C/(1+t**2)**0.5

ig = plt.figure(num=1)

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
