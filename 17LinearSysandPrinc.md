#线性微分方程组 
##微分方程建模回顾（例子）
有两个水罐:
* 左边的为1号，其中溶解有1000克盐的盐水100升，右边的为2号，其中溶解有500克盐的盐水200升。   
* 30克盐每升的盐水以每分钟2升的速度流入1号罐子；20克盐每升的盐水以每分钟4升的速度流入2号罐子。
* 1号罐子中的盐水以每分钟4升的速度流入2号罐子；2号罐子中的盐水以每分钟2升的速度流入1号罐子。
* 额外地，2号罐子中的盐水以每分钟3升的速度流到地上。
 
设1号罐子中的盐含量为$$x$$，而二号罐子中的盐含量为$$y$$,则描述上述信息的微分方程组为：
$$\frac{dx}{dt}=-4\times\frac{x}{100}+2\times\frac{dy}{dt}+2\times30$$
$$\frac{dy}{dt}=4\times\frac{x}{100}-5\times\frac{y}{200}+20\times 1$$
化简后获得：
$$\frac{dx}{dt}=-0.04x+0.01y+60$$
$$\frac{dy}{dt}=0.04x-0.025y+20$$

##线性方程组回顾
下面是一个线性方程组：
$$\frac{dx}{dt}=ax+by$$
$$\frac{dy}{dt}=cx+dy$$
其中自变量是$$x,y$$，$$a,b,c,d$$为系数。  

下面是一个二阶齐次线性方程
$$\alpha\frac{d^2x}{dt^2}+\beta\frac{dx}{dt}+\gamma{x}=0$$
其中$$\alpha,\beta,\gamma$$都是常数并且$$\alpha\neq{0}$$

我们令一个新的变量$$y$$对上面二阶齐次方程进行降次，获得如下线性方程组：
$$\frac{dx}{dt}=y$$
$$\frac{dy}{dt}=-\frac{\gamma}{\alpha}x-\frac{\beta}{\alpha}y$$ 

对于线性方程组，可以用向量形式来表示。令：
$$Y(t) = \begin{pmatrix} x(t) \ y(t) \end{pmatrix}$$  

对应的斜率场为：
$$F(Y) = F(\begin{pmatrix} x \ y \end{pmatrix}) = \begin{pmatrix} ax+by \ cx+dy \end{pmatrix}$$

$$\qquad = \begin{matrix} a b \ c d \end{matrix} \begin{matrix} x \ y \end{matrix}$$






