# 欧拉方法用于方程组
发现前几周已经不经意之间写了这个方法的程序。。。
$$\begin{cases} y(t_{i+1}) \approx y(t_{i}) + \frac{dy}{dt}\bigg|_{t=t_i} = y(t_{i}) + \frac{dy}{dt}\bigg|_{y=y(i), x = x(i)} \\ x(t_{i+1}) \approx x(t_{i}) + \frac{dx}{dt}\bigg|_{t=t_i} = x(t_{i}) + \frac{dx}{dt}\bigg|_{y=y(i), x = x(i)} \end{cases}$$

给定方程组：
$$\begin{cases} \frac{dx}{dt} = -y\\ \frac{dy}{dt} = x - y \end{cases},\qquad (x_0,y_0) = (2,0)$$    
选用步长$$\delta t = 0.5$$用欧拉方法进行近似：
```
    import numpy as np
    import sympy
    from sympy.abc import t
    from sympy import Function, Derivative, dsolve, Eq
    import matplotlib.pyplot as plt

    def numericalApproxForTwo(fR, fF, R0, F0, dt = 0.0005, steps = 300):
        tdomain = np.array([i*dt for i in range(steps)])

        Frange = [F0]
        Rrange = [R0]

        for t in tdomain[1:]:
            dR = fR.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
            dF = fF.subs({'R(t)':Rrange[-1] , 'F(t)': Frange[-1]})
            Rrange.append(Rrange[-1]+dt*dR)
            Frange.append(Frange[-1]+dt*dF)

        return tdomain, Rrange, Frange

    R = Function('R')
    F = Function('F')

    formulaR = -1*F(t)
    formulaF = R(t) -1*F(t)

    Tvals,Rvals,Fvals = numericalApproxForTwo(formulaR, formulaF, 2.0, 0.0, dt = 0.5, steps = 20)


    for i in range(4):
        print "%10s" % Rvals[i], "%10s" % Fvals[i]
```

