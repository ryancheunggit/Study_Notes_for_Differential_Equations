# ex1

k = ((76.3-5.3)/5.3)/100

print 76.3+76.3*k*100

# ex2
K=50
import math
k = math.log(20)/12
p18 = K*math.e**(18*k)

print p18

print math.log(2)/k

# ex3

from sympy.abc import p
import sympy
import numpy as np
import matplotlib.pyplot as plt
f = 0.3*(1-p/200)*(p/50-1)*p

domain = np.linspace(-30,210)

y = [f.subs(p,pval) for pval in domain]

plt.plot(domain,y)
plt.axhline(0,0,1, color = 'black')
plt.axvline(0,0,1, color = 'black')

print sympy.solve(f)




# ex6

from sympy.abc import p

pred = [2500.0]
logist = 0.3*p*(1-p/2500.0)-1/3.0*p
for i in range(999):
    pred.append(pred[-1]+pred[-1]*logist.subs(p,pred[-1]))
    if pred[-1] < 0:
        print "the population died out"
        break


# ex7

from sympy.abc import p
from sympy.abc import k
from sympy.abc import m
from sympy.abc import g
from sympy.abc import v

print sympy.solve(g-k*v**2/m,v)
