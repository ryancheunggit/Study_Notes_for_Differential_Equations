# libararies
import numpy as np
import matplotlib.pyplot as plt

# the data
USPop = np.array([3.9,5.3,7.2,9.6,12.9,
                  17.1,23.2,31.4,38.6,50.2,
                  63.0,76.3,92.0,105.7,122.8,
                  131.7,151.3,179.3,203.3,226.5,
                  248.7,281.4,308.7])

Year = np.array(range(1790,2011,10))

# plotting the data as scatter plot
plt.plot(Year,USPop,'bo')
plt.title("U.S. Census 1790-2010")

# library
import sympy
from sympy.abc import t
from sympy import E as e

# model
p = 3.9*e**(0.03067*t)

# domain
domain = np.array(range(0,len(USPop)*10,10))

# plot actual data and model prediction
plt.plot(Year,USPop,'bo')
plt.plot(Year,[p.subs(t,year) for year in domain])
# limit the y axis to see the lower part of the graph
plt.axis(ymax = 300)


# calculate relative growth rate
rgr = [1.0/USPop[i]*(USPop[i+1]-USPop[i-1])/20 for i in range(1,len(USPop)-1)]

# fit a line to the data
slope, intercept = np.polyfit(USPop[1:-1],rgr,1)
print slope, intercept

# make a plot
plt.plot(USPop[1:-1],rgr,'bo')
plt.plot(np.array(range(0,350)),slope*np.array(range(0,350))+intercept)
plt.text(344,0.001,'N',fontsize = 18,color="black")
plt.axis(ymin = 0)
plt.axis(xmax = 400)


# euler's method
from sympy.abc import p
pred = [3.9]
logistModel = intercept*p+slope*p**2
# step is 10
for i in range(22):
    pred.append(logistModel.subs(p,pred[-1])*10+pred[-1])

# make a plot
plt.plot(Year,USPop,'bo',Year,pred)


# plot the parabola
pdomain = np.array(range(-20,380,10))
plt.plot(pdomain, [logistModel.subs(p,pval) for pval in pdomain])
plt.axhline(0,0,1,linewidth = 2, color = 'black')
plt.axvline(0,0,1,linewidth = 2, color = 'black')
plt.text(342,0.001,'N',fontsize = 18,color="black")
plt.text(-20,2,r'$\frac{dp}{dt}$',fontsize = 18,color="black")
