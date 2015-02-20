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
    
    
    y = Function('y')
    avals = [0, 0.125, 0.25, 0.375]
    formula = y(t)*(1-y(t))-a
    
    bifurcationDiagram(formula, avals, np.linspace(-0.5,1.5), True)
```
![08-01phaseLines](images/08-01phaseLines.png)

如果将上图中各个红点链接起来就获得了**分歧图（bifurcation diagram）**，抛物线所向的一面是有平衡解的范围，相反则是无平衡解的范围，**分歧值（bifurcation value）**出现在$$a=\frac{1}{4}$$。称$$a<\frac{1}{4}$$的所有系统是**性质上等效（qualitatively equivalent）**，称$$a\geq \frac{1}{4}$$的所有系统是性质上等效的。

另一个例子：
$$\frac{dy}{dt}=y^3-ay$$  

![08-02bifurcationDiagram.png](images/08-02bifurcationDiagram.png)

绘制其分歧图，则只需要将上图中红点链接起来即可。







