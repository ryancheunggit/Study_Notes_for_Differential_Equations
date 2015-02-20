import sympy
from sympy.abc import t, a
from sympy import Function, Derivative, dsolve, Eq, solve

def narrowPhaseLine(formula, domain = np.linspace(-1,1), domainFix = False):
    solutions = solve(Eq(formula,0),y(t))
    try:
        solutions.sort()
        ran = solutions[-1]-solutions[0]
        if len(solutions) == 1:
            intervals = [solutions[0]-0.5, solutions[0], solutions[0]+0.5]
        else:
            intervals = [float(solutions[0]-0.25*ran)]+solutions+[float(solutions[-1]+0.25*ran)]

        if domainFix:
            ydomain = domain
        elif len(solutions) > 1:
            ydomain = np.linspace(float(solutions[0]-0.25*ran), float(solutions[-1]+0.25*ran))
        elif len(solutions) == 1:
            ydomain = np.linspace(float(solutions[0]-1),float(solutions[0]+1))
    except:
        if domainFix:
            ydomain = domain
        else:
            ydomain = np.linspace(-1,1)

        if 0 in solutions:
            signVals = [ydomain[12],ydomain[38]]
        else:
            signVals = [0]
        solutions = []

    fig = plt.figure(num=1, figsize=(1,4))
    plt.plot([0 for dummy in ydomain],ydomain, color = 'black')
    plt.plot([0 for dummy in solutions], solutions, 'or')
    plt.axis(xmin = -0.5, xmax = 0.5)

    if solutions != []:
        for i in range(len(intervals)-1):
            midpoint = (intervals[i]+intervals[i+1])/2.0
            intervalSign = sign(formula.evalf(subs={'y(t)':midpoint}))
            if intervalSign == -1:
                plt.text(0, midpoint, u'\u2193',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
            elif intervalSign == 1:
                plt.text(0, midpoint, u'\u2191',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
    else:
        for val in signVals:
            intervalSign = sign(formula.evalf(subs={'y(t)':val}))
            if intervalSign == -1:
                plt.text(0, val, u'\u2193',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
            elif intervalSign == 1:
                plt.text(0, val, u'\u2191',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)


y = Function('y')
avals = [0, -0.125, -0.25, -0.375]
formula = y(t)*(1-y(t))+a

for i in range(len(avals)):
    plt.subplot(1, len(avals), i+1)
    narrowPhaseLine(formula.subs(a, avals[i]), np.linspace(-0.5,1.5),True)


formula = y(t)**3-a*y(t)
avals = [-3, -2,-1, 0, 1, 2, 3]

for i in range(len(avals)):
    plt.subplot(1, len(avals), i+1)
    narrowPhaseLine(formula.subs(a, avals[i]),np.linspace(-3,3), True)
