import sympy
from sympy.abc import t
from sympy import Function
import matplotlib.pyplot as plt
y = Function('y')
formula = y(t)**2-t

def eulerMethod(formula,tval,yval,step,numSteps,percision = 5):
    tvals = [tval]
    yvals = [yval]
    for i in range(numSteps):
        m = round(formula.subs({y(t):yvals[-1],t:tvals[-1]}),percision)
        tvals.append(round(tvals[-1]+step,percision))
        yvals.append(round(yvals[-1]+m*step,percision))
        # print float(i)/numSteps*100
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


# ps 1
formula = (3-y(t))*(y(t)+1)
tv,yv = eulerMethod(formula,0, 4, 1.0, 10 ,5)
for i in range(len(tv)):
    print "after step {0} the t value is {1} and y value is {2}".format(str(i),str(tv[i]),str(yv[i]))

# ps 2
formula = sympy.E**(2.0/y(t))
tv,yv = eulerMethod(formula,0, 2, 0.5, 5 ,3)
for i in range(len(tv)):
    print "after step {0} the t value is {1} and y value is {2}".format(str(i),str(tv[i]),str(yv[i]))

# ps 3
formula = y(t)**2-y(t)**3
tv,yv = eulerMethod(formula,0, 0.2, 0.1, 100 ,3)
for i in range(len(tv)):
    print "after step {0} the t value is {1} and y value is {2}".format(str(i),str(tv[i]),str(yv[i]))

# ps 4
formula = 2*y(t)**3+t**2
tv,yv = eulerMethod(formula,0, -0.5, 0.1, 20 ,3)
yv[-1]

def eulerMethodNeg(formula,tval,yval,step,numSteps,percision = 5):
    tvals = [tval]
    yvals = [yval]
    for i in range(numSteps):
        m = round(formula.subs({y(t):yvals[-1],t:tvals[-1]}),percision)
        tvals.append(round(tvals[-1]-step,percision))
        yvals.append(round(yvals[-1]-m*step,percision))
        # print float(i)/numSteps*100
    return tvals, yvals

tv,yv = eulerMethodNeg(formula,0, -0.5, 0.1, 20 ,3)
yv[-1]

# ps 5

formula = y(t)**0.5
steps = [1.0, 0.5, 0.25]
for step in steps:
    tv,yv = eulerMethod(formula,0, 1, step, int(4.0/step) ,3)
    print yv[-1]

tdomain = np.linspace(0,20,30)
ydomain = np.linspace(0,100,30)

fg = plotEulerAndSF(formula, 0, 1, 0.01, tdomain, ydomain)
fg.show()

# ps 6
formula = 2 - y(t)
steps = [1.0, 0.5, 0.25]
for step in steps:
    tv,yv = eulerMethod(formula,0, 1, step, int(4.0/step) ,3)
    print yv[-1]

tdomain = np.linspace(0,20,30)
ydomain = np.linspace(0,4,30)

fg = plotEulerAndSF(formula, 0, 1, 0.01, tdomain, ydomain)
fg.show()

# ps 7

formula = (3 - y(t))*(y(t) + 1)
tv,yv = eulerMethod(formula,0, 0, 0.5, 10 ,2)

print yv[-1]

# ps 8

tdomain = np.linspace(0,5,30)
ydomain = np.linspace(0,5,30)
fg = plotEulerAndSF(formula, 0, 0, 0.5, tdomain, ydomain)
fg.show()

# ps 9

formula = 9.8 - 0.18/54.0*y(t)**2
from sympy import solve
vmax = solve(formula,y(t))[1]
tv,yv = eulerMethod(formula,0, 0, 0.01, 1500 ,3)
for i in range(len(yv)):
    if yv[i] >= 0.95*vmax:
        print 0+i*0.01
        break
