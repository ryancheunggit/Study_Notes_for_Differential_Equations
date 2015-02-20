import sympy
from sympy.abc import t, a
from sympy import Function, Derivative, dsolve, Eq, solve

y = Function('y')
avals = [0, -0.125, -0.25, -0.375]
formula = y(t)*(1-y(t))+a
domain = np.linspace(-0.5,1.5)
for i in range(len(avals)):
    plt.subplot(1, len(avals), i+1)
    phaseLine(formula.subs(a, avals[i]), [], domain, True)



formula = y(t)**3-a*y(t)
avals = [-3, -2,-1, 0, 1, 2, 3]
domain = np.linspace(-3,3)

for i in range(len(avals)):
    plt.subplot(1, len(avals), i+1)
    phaseLine(formula.subs(a, avals[i]), [], domain, True)


formula = y(t)**3-a*y(t)


def bifurcationDiagram(formula, avals, ydomain = np.linspace(-3,3)):
    fig = plt.figure(num=1)
    plt.axis(xmin = min(avals)-0.5, xmax = max(avals)+0.5)
    solutions = solve(formula,y(t))
    try:
        solutions.pop(solutions.index(0))
        for s in solutions:
            adomain = np.linspace(float(solve(s, a)[0]), max(avals))
            yvals = [s.subs(a,aval) for aval in adomain]
            plt.plot(adomain, yvals, color = 'blue')
    except:
        None


    for aval in avals:
        formli = formula.subs(a, aval)
        solutions = solve(Eq(formli,0),y(t))
        try:
            solutions.sort()
            ran = solutions[-1]-solutions[0]
            if len(solutions) == 1:
                intervals = [solutions[0]-0.5, solutions[0], solutions[0]+0.5]
            else:
                intervals = [float(solutions[0]-0.25*ran)]+solutions+[float(solutions[-1]+0.25*ran)]
        except:
            if 0 in solutions:
                signVals = [ydomain[12],ydomain[38]]
            else:
                signVals = [0]
            solutions = []


        plt.plot([aval for dummy in ydomain],ydomain, color = 'black')
        plt.plot([aval for dummy in solutions], solutions, 'or')

        if solutions != []:
            for i in range(len(intervals)-1):
                midpoint = (intervals[i]+intervals[i+1])/2.0
                intervalSign = sign(formli.evalf(subs={'y(t)':midpoint}))
                if intervalSign == -1:
                    plt.text(aval, midpoint, u'\u2193',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
                elif intervalSign == 1:
                    plt.text(aval, midpoint, u'\u2191',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
        else:
            for val in signVals:
                intervalSign = sign(formli.evalf(subs={'y(t)':val}))
                if intervalSign == -1:
                    plt.text(aval, val, u'\u2193',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
                elif intervalSign == 1:
                    plt.text(aval, val, u'\u2191',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
    return fig



formula = y(t)**3+a*y(t)
avals = [-3, -2,-1, 0, 1, 2, 3]
domain = np.linspace(-3,3)
bifurcationDiagram(formula, avals, domain)


# ex2

formula = (y(t)**2-a)*(y(t)**2-4)
avals = [0, 1, 2, 3, 4, 5]
domain = np.linspace(-4,4)
bifurcationDiagram(formula, avals, domain)


# ex4
formula = y(t)**2+3*y(t)+a
avals = [0,3.0/4,6.0/4,9.0/4,13.0/4]
domain = np.linspace(-5,3.5)


bifurcationDiagram(formula, avals, domain)

# ex6

formula = 4*y(t)-y(t)**2
avals = [-3,-2,-1, 0,1,2,3]
domain = np.linspace(-5,5)
bifurcationDiagram(formula, avals, domain)

formula = 4+y(t)**2
avals = [-4,-2,0,2,4,6]
domain = np.linspace(-5,5)
bifurcationDiagram(formula, avals, domain)
