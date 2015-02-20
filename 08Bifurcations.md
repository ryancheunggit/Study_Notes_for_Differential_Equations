#**分歧（Bifurcations）**  
本节关注的是，根据参数值的不同，微分方程解的长远表现会有怎样的不同。  

分歧：参数值发生很小变化，解的长远表现发生很大的变化。

回顾之前介绍的罗吉斯特增长模型：
$$\frac{dP}{dt}=kP(1-\frac{P}{N})$$    
现假设用该模型描述养鱼场鱼类的繁殖，并考虑加入一个每年固定的捕鱼率$$C$$：
$$\frac{dP}{dt}=kP(1-\frac{P}{N})-C$$    
模型中参数有3个：$$k,N$$和$$C$$，假设$$k,N$$均限定不变，只余$$C$$是可变的，考察改变$$C$$的值，对方程解的长远表现有何影响。  

首先考虑到$$kP(1-\frac{P}{N})$$是开口朝下的抛物线，若要方程有平衡解，则需要$$C$$小于抛物线的最大值，即：  
$$C\leq \frac{kN}{4}$$  

考虑同类型方程中更简单一点的例子：  
$$\frac{dy}{dt}=y(1-y)-a$$  
其中$$a$$为参数,试看调整$$a$$的值，导致的相线变化： 

```
    import sympy
    from sympy.abc import t, a
    from sympy import Function, Derivative, dsolve, Eq, solve
    
    def narrowPhaseLine(formula, domain = None):
        solutions = solve(Eq(formula,0),y(t))
        try:
            solutions.sort()
            ran = solutions[-1]-solutions[0]
            if not domain and len(solutions) > 1:
                ydomain = np.linspace(float(solutions[0]-0.25*ran), float(solutions[-1]+0.25*ran))
            if not domain and len(solutions) == 1:
                ydomain = np.linspace(solutions[0]-1,solutions[0]+1)
            if domain:
                ydomain = domain
            intervals = [float(solutions[0]-0.25*ran)]+solutions+[float(solutions[-1]+0.25*ran)]
        except:
            solutions = []
            if not domain:
                ydomain = np.linspace(-1,1)     
            if domain:
                ydomain = domain   
    
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
            intervalSign = sign(formula.evalf(subs={'y(t)':0}))
            if intervalSign == -1:
                plt.text(0, 0, u'\u2193',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
            elif intervalSign == 1:
                plt.text(0, 0, u'\u2191',fontname='STIXGeneral', color = 'blue', size=30, va='center', ha='center', clip_on=True)
            
            
    y = Function('y')
    avals = [0, -0.125, -0.25, -0.375]
    formula = y(t)*(1-y(t))+a
    
    for i in range(len(avals)):
        plt.subplot(1, 4, i+1)
        narrowPhaseLine(formula.subs(a, avals[i]))
```
![08-01phaseLines](images/08-01phaseLines.png)

