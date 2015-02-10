#欧拉方法  
给定一个微分方程和初值：
$$\frac{dy}{dt}=y^2-t, y(0)=0$$   
在不求解的前提下，想要获得一个近似解，最简单的方法之一是欧拉方法。  
欧拉方法中，我们设定一个**步长（step size）**$$\delta t$$，依据线性近似的公式：  
$$y(t_{i+1})=y(t_i + \Delta t)=y(t)+\frac{dy}{dt}\bigg|_{t=t_i}\Delta t+O({\Delta t}^2)\\
\qquad \approx y(t)+\frac{dy}{dt}\bigg|_{t=t_i}\Delta t$$  
迭代地获得解的近似。  

Python中定义欧拉方法：
```
    import sympy
    from sympy.abc import t
    from sympy import Function
    y = Function('y')
    formula = y(t)**2-t

    def eulerMethod(formula,tval,yval,step,numSteps):
        tvals = [tval]
        yvals = [yval]
        for i in range(numSteps):
            m = formula.subs({y(t):yvals[-1],t:tvals[-1]})
            tvals.append(tvals[-1]+step)
            yvals.append(yvals[-1]+m*step)
        return tvals, yvals


    tv,yv = eulerMethod(formula, -1.0, -0.5,0.5,4)
    for i in range(len(tv)):
        print "after step {0} the t value is {1} and y value is\
        {2}".format(str(i),str(tv[i]),str(yv[i]))
    
    # output is :
    # after step 0 the t value is -1.0 and     y value is -0.5
    # after step 1 the t value is -0.5 and     y value is 0.125000000000000
    # after step 2 the t value is 0.0 and     y value is 0.382812500000000
    # after step 3 the t value is 0.5 and     y value is 0.456085205078125
    # after step 4 the t value is 1.0 and     y value is 0.310092062223703
```




