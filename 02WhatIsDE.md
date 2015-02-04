#什么是微分方程
##**什么是一阶微分方程？**  
$$\frac{dy}{dt}=f(t,y(t))$$   
初一看可能会觉得奇怪，因为左边$$\frac{dy}{dt}$$是关于$$t$$的函数，而右边是关于$$t$$和$$y$$的函数，但是注意到$$y$$是$$t$$的函数，因此是没有问题的。  

##**什么是初值问题（initial value problem）？**    
给定$$\frac{dy}{dt}=f(t,y(t))$$，以及$$y(t_0)=y_0$$的问题。   

##**注意符号**    
微分方程$$\frac{dy}{dt}=2t$$的解为:$$y(t)=t^2+C$$  
微分方程$$\frac{dy}{dt}=2y$$的解为:$$y(t)=y_0e^{2t}$$  

##**一般解（general solution）是什么？**    
像上面的解中，$$C$$和$$y_0$$的取值为任意合理值，则解为一般解。

##**检查方法**  
可以通过求导的方法来验证一个微分方程的解是否正确。

##**Python**

求导函数：  

```
	import sympy
	from sympy.abc import t
	sympy.diff(1/(t**2+1),t)
	# result : -2*t/(t**2 + 1)**2
```


已知微分方程：$$\frac{dy}{dt}=2y+1$$，检验$$y(t)=3e^{2t}-1/2$$是否为其解
```
	from sympy import E as E
	y = 3*E**(2*t)-1.0/2
	print sympy.diff(y,t) == 2*y+1
	# result is: True
```

用Matlab求微分方程的解：
$$\frac{dw}{dt}=w$$  
```
	w = dsolve('Dw=w')
```
Python中:

```
	from sympy import Function, dsolve, Derivative
	w = Function('w')
	dsolve(Derivative(w(t),t)-w(t),w(t))
	# result is: w(t) == C1*exp(t)
```

