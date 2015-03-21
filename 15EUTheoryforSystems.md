# 方程组解的存在性和唯一性
给定方程组：
$$\frac{dY}{dt} = F(t, Y)$$  
和初值$$t_0, Y_0$$     
假设函数$$F$$是连续可分的，则：   
存在一个$$\epsilon > 0$$和函数$$Y(t)$$定义在$$t_0 - \epsilon < t < t_0 + \epsilon$$ 使得：   
$$\frac{dY}{dt} = F(t, Y(t))$$  
并且
$$Y(t_0) = Y_0$$   
即：$$Y(t)$$是满足初值的一个解，并且当$$t$$在上述范围内时，该解是唯一解。   

如果给定的方程组是一个自治方程组，即：   
$$\frac{dY}{dt} = F(Y)$$    
假设$$Y_0$$是相位平面内的一点，$$Y_1(t)$$是满足初值条件$$Y(t_1)=Y_0$$的一个解，$$Y_2(t)$$是满足初值条件$$Y(t_2)=Y_0$$的一个解，那么：  
$$Y_2(t) = Y_1(t - (t_2-t_1))$$  
例如：
$$\frac{d^2x}{dt^2} + x = 0$$   
等同于如下自治方程组：  
$$\begin{cases} \frac{dx}{dt} = y \\ \frac{dy}{dt} = -x \end{cases}$$  
该方程组有如下两个特殊解：  
$$Y_1(t) = \begin{pmatrix} cost \\ - sint \end{pmatrix}$$

$$Y_2(t) = \begin{pmatrix} sint \\ cost \end{pmatrix}$$  

注意到$$Y_1(0) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$，$$Y_2(\frac{\pi}{2}) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$    
则有：    
$$Y_1(t-\frac{\pi}{2}) = Y_2(t)$$    



