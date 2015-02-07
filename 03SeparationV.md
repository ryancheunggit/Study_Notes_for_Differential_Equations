#分离变量法（Separation of Variables）    
##**1 换元积分法（Method of Substitution）**    
例1：计算$$\int(cost^2)dt$$  
这个不定积分非常困难，其结果包含Fresnel $$C$$函数。  
```
    import sympy
    from sympy.abc import t
    print sympy.integrate(sympy.cos(t**2),t)
    # result is: sqrt(2)*sqrt(pi)*fresnelc(sqrt(2)*t/sqrt(pi))*gamma(1/4)/(8*gamma(5/4))
```

例2：计算$$\int(cost^2)(2t)dt$$  
这个不定积分就简单得多，可以用换元积分法来求解。  
令：$$u=t^2,du=2tdt$$  
则：$$\int(cost^2)(2t)dt=\int(cosu)du\\
\ =sinu+C\\
\ =sint^2+C$$  

```
    print sympy.integrate(sympy.cos(t**2)*2*t,t)
    # result is: sin(t**2)
```

一般地，换元积分法表示为：  
$$\int g(u)(\frac{du}{dt})dt = \int g(u)du \\
\ = G(u) + k$$  
其中：$$G'(u)=g(u)$$  

练习： 
$$\int \frac{4x}{1+4x^2}dx$$  
换元方法：  
$$g(u)=\frac{1}{u},\qquad G(u)=ln(u)\\
\ u={1+4x^2}\\
\ du=8xdx$$  
$$\int \frac{4x}{1+4x^2}dx=\frac{1}{2}\int \frac{1}{1+4x^2}8xdx\\
\qquad = \frac{1}{2} \int g(u)du\\
\qquad = \frac{1}{2} ln(u)+C\\
\qquad = \frac{1}{2} ln(1+4x^2)+C$$    

##**2 可分方程（separable equations）**  
微分方程$$\frac{dy}{dt}=f(t,y)$$若能写成$$\frac{dy}{dt}=(f_1{(t)})(f_2{(y)})$$的形式，则称为可分方程。  

可分方程可以通过分变量的方法通过换元方法"求解"：  
$$\frac{dy}{dt}=(f_1{(t)})(f_2{(y)})\\
(\frac{1}{f_2{(y)}})(\frac{dy}{dt})=f_1{(t)}$$    
令$$g(y)=(\frac{1}{f_2{(y)}})$$
则有：$$g(y)(\frac{dy}{dt})=f_1{(t)}$$，两边同时针对$$t$$积分:  
$$\int g(y)(\frac{dy}{dt})dt=\int f_1{(t)}dt\\
\int g(y)dy=\int f_1{(t)}dt$$  

例1：
$$\frac{dy}{dt}=-2ty^2\\
\ =(-2t)(y^2)$$  
是可分的 

```
	from sympy.abc import y
	f = -2*t*y**2
	print sympy.separatevars(f, symbols=(t,y))
	# result is : -2*t*y**2
```

例2：
$$\frac{dy}{dt}=y^3+t^2$$
是不可分的  

```
	print sympy.separatevars(y**3+t**2, symbols=(t,y))
	# result is : t**2 + y**3
```

练习:
$$\frac{dy}{dt}=ty+ty^2$$  
```
	print sympy.separatevars(t*y+t*y**2, symbols=(t,y))
	# result is : t*y*(y + 1)
```

$$\frac{dy}{dt}=t^2y+ty^2$$
```
	print sympy.separatevars(t**2*y+t*y**2, symbols=(t,y))
	# result is : t*y*(t + y)
```

##**3 可分方程的求解**

方程可分，并不表示真正可解，拆分成$$\int g(y)dy=\int f_1{(t)}dt$$形式后，仍需要两边的积分可求解才行。

$$\frac{dy}{dt}=-2ty^2=(-2t)(y^2)\\
\ (\frac{1}{y^2})(\frac{dy}{dt})=-2t\\
\ \int \frac{1}{y^2}dy=\int -2tdt\\
\ -1\frac{1}{y}=-t^2+C\\
\ y^{-1}=t^2+C\\
\ y(t)=\frac{1}{t^2+C}
$$  

练习（初值问题）：
若给定$$y(0)=\frac{1}{2}$$，则：$$c=2,y(t)=\frac{1}{t^2+2}$$   
其定义域为：$$t\in (-\infty, \infty)$$

若给定$$y(0)=-\frac{1}{2}$$，则：$$c=-2,y(t)=\frac{1}{t^2-2}$$   
其定义域为：$$-\sqrt{2}<t<\sqrt{2}$$
若给定$$y(-2)=\frac{1}{2}$$，则：$$c=-2,y(t)=\frac{1}{t^2-2}$$   
其定义域为：$$-\infty<t<-\sqrt{2}$$
若给定$$y(2)=\frac{1}{2}$$，则：$$c=-2,y(t)=\frac{1}{t^2-2}$$   
其定义域为：$$\sqrt{2}<t<\infty$$
虽然这三个解的形式相同，但初值不同，定义域不同，因此是三个不同的解。

另外$$\forall t, y(t)=0$$也满足微分方程，称为**平衡解（equilibrium solution）**。   
因此两者合起来才是该微分方程的一般解。    

练习：
$$\frac{dy}{dt}=2ty^2+3y^2\\
\frac{1}{y^2}\frac{dy}{dt}=2t+3\\
\int \frac{1}{y^2}dy = \int (2t+3)dt\\
-1\frac{1}{y}=t^2+3t+c\\
y(t)=-1\frac{1}{t^2+3t+C}
$$    

另外$$y(t)=0$$也满足。  

```
	from sympy import Function, dsolve, Derivative
	y = Function('y')
	dsolve(Derivative(y(t),t)-2*t*(y(t))**2-3*(y(t))**2,y(t))
	# result is :  y(t) == -1/(C1 + t**2 + 3*t)
```

