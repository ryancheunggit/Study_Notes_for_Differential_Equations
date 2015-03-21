# SIR流行病模型 
模型由Kermack和McKendrick发明。模型中将人群分为下面三组：
1. 易受到感染的 susceptible 
2. 感染了的 infective
3. 病好了的 removed

1前提假设：
 * 1人口总数是常数
 * 2感染人群的数量增长率与（感染人群和易受感染人群数量和）成正比
 * 3易受感染人群的数量减少与上面相同
 * 4感染人群中人们祛病的速率与受感染人群总数成正比
 * 5潜伏期非常短，可以被忽略
 * 6三组人是平均分布的，即：每个人都有同样的概率与任意一个人接触

2变量：
 * 时间t
 * S(t)
 * I(t)
 * R(t)

3模型：
 * 由假设2,3,4有：$$\frac{dS}{dt} = - \alpha SI$$,$$\qquad \alpha$$为感染参数
 * 由假设2,4,6有：$$\frac{dI}{dt} = \alpha SI - \beta I$$, $$\qquad \beta$$为祛病率
 * 由假设1,4有：$$\frac{dR}{dt} = \beta I$$

三者结合获得模型:
$$\begin{cases} \frac{dS}{dt} = - \alpha SI \\ \frac{dI}{dt} = \alpha SI - \beta I \\ \frac{dR}{dt} = \beta I \end{cases}$$   

因为人口总数是常数，我们知道：
$$\frac{dS}{dt}+\frac{dR}{dt}+ \frac{dI}{dt} = 0$$    
$$S(t)+I(t)+R(t) = N, \text{for all t}$$    
其中任意一个方程都可以由另外两个方程的线性组合获得，因此让我们集中注意于二维平面。  
$$\begin{cases} \frac{dS}{dt} = - \alpha SI \\ \frac{dI}{dt} = \alpha SI - \beta I \end{cases}$$   

尝试寻找一下模型的平衡解吧：
若要$$\frac{dS}{dt} = - \alpha SI$$则，要么$$S(t)=0$$或者$$I(t)=0$$。
若要$$\alpha SI - \beta I = I(\alpha S - \beta) = 0$$则需要：$$I = 0$$或者$$S = \frac{\beta}{\alpha}$$  

简单分析下模型：
因为$$\alpha, \beta, S, I, R$$都是非负的，因此$$S(t)$$是非增的，$$R(t)$$是非减的，而$$I(t)$$的增减性取决于1$$I$$是否为零；2$$\alpha S - \beta$$的符号正负。

这个$$S = \frac{\beta}{\alpha} = \rho$$是一个阈值，决定了$$I(t)$$的增减性。 
也就是说一旦易受感染的人数$$S$$大于阈值，受感染的人数就会增加；一旦易受感染的人数$$S$$小于阈值，受感染的人数就会减少。   

下面是一个事实：
方程组$$SI$$平面内的解曲线满足如下等式：    
$$I+S-\rho ln(S) = \text{constant}$$  
可以用初值以及$$I_{max}$$时的$$S = \rho$$来求解最大感染人数$$I_{max}$$  
$$I_{max} + \rho -\rho ln(\rho)= I_0 + S_0 - \rho ln(S-0)$$   
代入数据即可求得$$I_{max}$$
