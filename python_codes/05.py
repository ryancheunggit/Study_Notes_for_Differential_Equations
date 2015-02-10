import sympy
from sympy.abc import t
from sympy import Function
y = Function('y')
formula = y(t)**2-t

def eulerMethod(formula,tval,yval,step,numSteps,percision = 5):
    tvals = [tval]
    yvals = [yval]
    for i in range(numSteps):
        m = round(formula.subs({y(t):yvals[-1],t:tvals[-1]}),percision)
        tvals.append(round(tvals[-1]+step,percision))
        yvals.append(round(yvals[-1]+m*step,percision))
        print float(i)/numSteps*100
    return tvals, yvals


tv,yv = eulerMethod(formula, -1.0, -0.5,0.5,4)
for i in range(len(tv)):
    print "after step {0} the t value is {1} and \
    y value is {2}".format(str(i),str(tv[i]),str(yv[i]))

# exercise 1
tv,yv = eulerMethod(formula, -1.0, -1.0 ,0.5,4)
for i in range(len(tv)):
    print "after step {0} the t value is {1} and y value is {2}".format(str(i),str(tv[i]),str(yv[i]))

# exercise 2
formula = y(t)**2-t**2
tv,yv = eulerMethod(formula, -2.0, -1.0 ,0.1,40)
for i in range(len(tv)):
    print "after step {0} the t value is {1} and y value is {2}".format(str(i),str(tv[i]),str(yv[i]))


# plot
import numpy as np
tdomain = np.linspace(0,7,30)
ydomain = np.linspace(-3*np.pi,3*np.pi,30)
step = 0.05
tval = 0
yval = 5

formula = sympy.E**(t)*sympy.sin(y(t))

def plotEulerAndSF(formula,tval,yval,step, tdomain, ydomain,percision=5):
    fig = plt.figure(num=1)
    numIter = int(float(tdomain[-1]-tdomain[0])/step)
    tv,yv = eulerMethod(formula, tval, yval ,step, numIter,percision)

    T,Y = np.meshgrid(tdomain,ydomain)
    U = 1
    V = np.array([[formula.subs({y(t): yval, t: tval}) for tval in tdomain] for yval in ydomain],dtype = 'float')
    N = np.sqrt(U**2+V**2)
    U2, V2 = U/N, V/N
    plt.quiver( T,Y,U2, V2)
    plt.plot(tv,yv)
    plt.xlim([tdomain[0],tdomain[-1]])
    plt.ylim([ydomain[0],ydomain[-1]])


    return fig

fg = plotEulerAndSF(formula, tval, yval, 0.05, tdomain, ydomain)
fg.show()
