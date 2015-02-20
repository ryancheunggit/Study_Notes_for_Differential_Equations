import sympy
from sympy.abc import t
from sympy import Function, Derivative, dsolve, Eq, solve

def phaseLine(formula):

    solutions = solve(Eq(formula,0),y(t))
    solutions.sort()
    ran = solutions[-1]-solutions[0]
    ydomain = np.linspace(float(solutions[0]-0.25*ran), float(solutions[-1]+0.25*ran))

    fig = plt.figure(num=1)
    plt.plot([0 for dummy in ydomain],ydomain, color = 'black')
    plt.plot([0 for dummy in solutions], solutions, 'or')
    plt.axis(xmin = -0.5, xmax = 0.5)

    intervals = [float(solutions[0]-0.25*ran)]+solutions+[float(solutions[-1]+0.25*ran)]
    for i in range(len(intervals)-1):
        midpoint = (intervals[i]+intervals[i+1])/2.0
        intervalSign = sign(formula.evalf(subs={'y(t)':midpoint}))
        if intervalSign == -1:
            plt.text(0, midpoint, u'\u2193',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
        elif intervalSign == 1:
            plt.text(0, midpoint, u'\u2191',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
    return fig



y = Function('y')
formula = y(t)*(1-y(t))
fg = phaseLine(formula)
fg.show()


# exercise
formula = y(t)**2 - 4*y(t) - 12
fg2 = phaseLine(formula)
fg2.show()

# exercise
formula = 3*y(t)**3-12*y(t)**2
fg3 = phaseLine(formula)
fg3.show()


def phaseLine(formula, solutions = None):
    if solutions == None:
        solutions = solve(Eq(formula,0),y(t))
        solutions.sort()

    ran = solutions[-1]-solutions[0]

    ydomain = np.linspace(float(solutions[0]-0.25*ran), float(solutions[-1]+0.25*ran))

    fig = plt.figure(num=1)
    plt.plot([0 for dummy in ydomain],ydomain, color = 'black')
    plt.plot([0 for dummy in solutions], solutions, 'or')
    plt.axis(xmin = -0.5, xmax = 0.5)

    intervals = [float(solutions[0]-0.25*ran)]+solutions+[float(solutions[-1]+0.25*ran)]
    for i in range(len(intervals)-1):
        midpoint = (intervals[i]+intervals[i+1])/2.0
        intervalSign = sign(formula.evalf(subs={'y(t)':midpoint}))
        if intervalSign == -1:
            plt.text(0, midpoint, u'\u2193',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
        elif intervalSign == 1:
            plt.text(0, midpoint, u'\u2191',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
    return fig





formula = y(t)**2*sympy.cos(y(t))
fg4 = phaseLine(formula)
fg4.show()

fg5 = phaseLine(formula, [-3/2.0*pi,-1.0/2*pi,0,1.0/2*pi,3/2.0*pi])
fg5.show()


# ps 2
formula = (1-y(t))*sympy.sin(y(t))
phaseLine(formula, [-2.0*pi,-1.0*pi,0, 1.0, pi,2.0*pi])


def phaseLine(formula, domain = np.linspace(-1,1), domainFix = False):
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
    return fig
