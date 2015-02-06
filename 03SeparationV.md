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
\qquad = \int g(u)du\\
\qquad = ln(u)+C\\
\qquad = ln(1+4x^2)+C$$    

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

##**3 **