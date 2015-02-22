# 9 线性微分方程
## 9.1 **线性（linearity）**  
### 例子
考虑如下问题：
一个容积$$200$$升的容器中有$$100$$升盐水，盐的含量为$$1000$$克。假设盐浓度35克每升的盐水以每分钟$$4$$升的速度注入容器，完全混合的溶液以每分钟$$2$$升的速度流出。  
用微分方程描述该容器内盐的含量，则盐含量的变化率为盐流入的速率减去盐流出的速率：  
$$\frac{ds}{dt}=\text{rate in}-\text{rate out}\\
\qquad = 35*4 - 2\frac{s}{100+(4-2)t}\\
\qquad = 140 - \frac{s}{50+t}$$

加上$$s(0)=1000$$，我们便获得了一个初值问题。

本节内容便是讨论如何解这一类的微分方程。

### 线性微分方程
我们称一阶微分方程$$\frac{dy}{dt}=f(t,y)$$是线性的，如果其可以写成如下形式：
$$\frac{dy}{dt}=a(t)y+b(t)$$  
即右边能写成因变量(这里是$$y$$)的线性函数的形式。  

### 齐次与非齐次
对于线性微分方程，又分两大类:
1. **齐次（homogeneous）**，$$b(t)=0$$  
2. **非齐次（nonhomogeneous）**$$b(t)\neq 0$$  

例如：
+ 线性且齐次：$$\frac{dy}{dt}=(cost)y$$  
+ 线性非齐次：$$\frac{dy}{dt}=y-t^2$$  
+ 非线性： $$\frac{dy}{dt}=y^2$$  

我们上面获得的盐水问题就是线性非齐次的。

### 线性齐次=可分
注意到线性齐次微分方程式是我们之前所提到的可分微分方程，可以通过两边同除以$$y$$后同时积分的方法来求解。  

$$\frac{dy}{dt}=a(t)y\\
\frac{1}{y}\frac{dy}{dt}=a(t)\\
\int \frac{1}{y}dy = \int a(t)dt$$    

看一个具体的线性齐次微分方程的例子：
$$\frac{dy}{dt}=\frac{-ty}{1+t^2}\\
\frac{1}{y} \frac{dy}{dt} = \frac{-t}{1+t^2} \\
\int \frac{1}{y} dy = \int \frac{-t}{1+t^2} dt \\
ln(|y|) = -\frac{1}{2}ln(1+t^2) + C\\
ln(|y|) = ln(\frac{1}{1+t^2}) + C\\
|y| = (\frac{1}{\sqrt{1+t^2}})(e^C)\\
y = (\frac{1}{\sqrt{1+t^2}})(C)\\
y(t) = \frac{C}{\sqrt{1+t^2}}$$  

斜率场和若干个解的图如：  

```
    tdomain = np.linspace(-3,3,30)
    ydomain = np.linspace(-5,5,30)
    
    y = Function('y')
    formula = -1*t*y(t)/(1+t**2)
    
    fg = plotSlopeField(tdomain,ydoman,formula,[(0,4),(0,3),(0,2),(0,1),(0,-1),(0,-2),(0,-3),(0,-4)])
    
    fg.show()
```

![09-01slopeFieldofHomo](images/09-01slopeFieldofHomo.png)

可以看出其各个解之间的差距只是$$k$$值得不同。如果获得了一个解，便可以通过乘以一个值得方法来获得任何一个其他解。  

### **齐次微分方程的线性原理（The Linearity Principle for Homogeneous Equations）**  
如果$$y_h(t)$$是一个齐次线性微分方程$$\frac{dy}{dt}=a(t)y$$的解，那么将其乘以任何一个常数$$k$$获得的$$y_k(t)=ky_h(t)$$也同样是一个解。  

检该原理非常简单：

$$\frac{dy_k}{dt}=k(\frac{dy_h}{dt})\\
\qquad = k(a(t)y_h)\\
\qquad = a(t)(ky_h)\\
\qquad = a(t)(y_k(t))$$  

###**一阶方程的扩展线性原理(The Extended Linearity Principle for First-Order Equations)**

考虑一个一阶非齐次线性方程：
$$\frac{dy}{dt}=a(t)y + b(t)$$   
以及其对应的齐次方程：
$$\frac{dy}{dt}=a(t)y$$   

1. 如果$$y_h(t)$$是齐次方程的任意一个解，而$$y_p(t)$$是相应的非齐次方程的任意一个解，那么$$y_h(t)+y_p(t)$$也是该非齐次方程的一个解。   
2. 若$$y_h(t)$$和$$y_p(t)$$分别是非齐次方程的两个解，那么$$y_h(t)-y_p(t)$$是相应齐次方程的一个解。  

因此，如果$$y_h(t)$$非零，则$$ky_h(t)+y_p(t)$$是非齐次方程的一般解。  

即：

**一个非齐次线性方程的一般解可由（非齐次方程的任意一个解）和（相应齐次方程的一般解）相加获得**   
    
例子，非齐次线性方程：
$$\frac{dy}{dt}=\frac{-ty}{1+t^2}+\frac{2t^2+1}{4t^2+4}$$  
现在知道其有一个特殊解$$y_p(t)=\frac{t}{4}$$  

通过上面，我们已经知道对应的齐次线性方程的一般解为：
$$y(t) = \frac{C}{\sqrt{1+t^2}}$$

因此上述非齐次方程的其一般解为:
$$y(t) = \frac{t}{4} + \frac{C}{\sqrt{1+t^2}}$$

```
    from sympy.abc import C
    formula = -1*t*y(t)/(1+t**2) + (2*t**2+1)/(4*t**2+4)
    solutions = t/4+C/(1+t**2)**0.5
    points = [(0,4),(0,3),(0,2),(0,1),(0,-1),(0,-2),(0,-3),(0,-4)]
    
    
    fig = plt.figure(num=1)
    # create grid
    T,Y = np.meshgrid(tdomain,ydomain )
    # calculate slope vectors
    U = 1
    V = np.array([[formula.subs({y(t): yval, t: tval}) for tval in tdomain] for yval in ydomain],dtype = 'float')
    N = np.sqrt(U**2+V**2)
    U2, V2 = U/N, V/N
    # make the plot
    plt.quiver( T,Y,U2, V2)
    plt.xlabel(r"$t$")
    plt.ylabel(r"$y$")
    plt.axhline(0,0,1,linewidth = 2, color = 'black')
    plt.axvline(0,0,1,linewidth = 2, color = 'black')
    
    for p in points:
        Cval = solve(Eq(solutions.subs(t,p[0]),p[1]))[0]
        solution = solutions.subs(C,Cval)
        plt.plot(tdomain, np.array([solution.subs(t,tval) for tval in tdomain],dtype= 'float'),
                        linewidth = '2')
    
            # limiting the axes
        plt.xlim([tdomain[0],tdomain[-1]])
        plt.ylim([ydomain[0],ydomain[-1]])
```

![09-02slopeFieldofNonHomo](images/09-02slopeFieldofNonHomo.png)

这个非齐次的线性方程的斜率场和解，可以看成是对应的齐次线性方程斜率场合解调整后的结果。  

例题：
若已知$$y()\frac{a}{t^2}$$是微分方程$$\frac{dy}{dt}=2ty-\frac{6}{t^2}-\frac{6}{t^3}$$的一个特殊解，求$$a$$的值。






