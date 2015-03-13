# 特殊方程组的分析解法
我们很少能用分析解法求解微分方程组，但还是有些是可解的。   

考虑如下方程组，和初值：
$$\begin{cases} \frac{dx}{dt} = 2y-x \\ \frac{dy}{dt} = y \end{cases}, \qquad (x_0, y_0) = (2,1) $$

其斜率场和解如下图：
```
    import numpy as np
    import sympy
    from sympy.abc import t
    from sympy import Function, Derivative, dsolve, Eq
    import matplotlib.pyplot as plt
        
    def directionField(fR, fF, Rdomain, Fdomain):
        fig = plt.figure(num=1)
        Rvals,Fvals = np.meshgrid(Rdomain,Fdomain)
        r = np.array([[fR.subs({'R(t)':rval, 'F(t)':fval}) for rval in Rdomain] for fval in Fdomain],dtype = 'float')
        f = np.array([[fF.subs({'R(t)':rval, 'F(t)':fval}) for rval in Rdomain] for fval in Fdomain],dtype = 'float')
        n = np.sqrt(r**2+f**2)
        r, f = r/n, f/n
        plt.quiver(Rvals, Fvals, r, f)
        plt.xlabel(r"$R$")
        plt.ylabel(r"$F$")
        plt.axhline(0,0,1,linewidth = 2, color = 'black')
        plt.axvline(0,0,1,linewidth = 2, color = 'black')
        return fig

    R = Function('R')
    F = Function('F')

    formulaR = 2*F(t) - R(t)
    formulaF = R(t)

    Rdomain = np.linspace(-1,10,30)
    Fdomain = np.linspace(-1,10,30)

    fg1 = directionField(formulaR, formulaF,Rdomain, Fdomain)
    tdomain = np.linspace(-2.2,2.2,30)
    Rvals = [exp(t) + exp(-1*t) for t in tdomain]
    Fvals = [exp(t) for t in tdomain]
    plt.plot(Rvals, Fvals, linewidth = 2)
    fg1.show()
```

![13-01ExampleSystem](images/13-01ExampleSystem.png)    

其成分图为：
```
    fg2 = plt.figure()
    plt.plot(tdomain, Rvals, 'r', tdomain, Fvals, 'b')
    fg2.show()
```
![13-01ExampleComponent](images/13-01ExampleComponent.png)

注意到$$y(t)$$的成分图看上去像是一个指数函数，$$x(t)$$看上去像是一个抛物线。  

实际上，其解为：
$$Y(t) = \begin{pmatrix} e^t + e^{-t} \\ e^t \end{pmatrix} $$  
检验一下：
$$\frac{dY}{dt} = \begin{pmatrix} e^t -e^{-t}\\ e^t \end{pmatrix}$$  
$$F(Y(t)) = \begin{pmatrix} 2e^t - (e^t + e^{-t})\\ e^t \end{pmatrix} = \begin{pmatrix} e^t -e^{-t}\\ e^t \end{pmatrix}$$
并且$$Y(0) = \begin{pmatrix}  2\\1 \end{pmatrix}$$    

