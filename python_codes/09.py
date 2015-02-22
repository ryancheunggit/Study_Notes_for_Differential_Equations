# slope field

tdomain = np.linspace(-3,3,30)
ydomain = np.linspace(-5,5,30)

y = Function('y')
formula = -1*t*y(t)/(1+t**2)

fg = plotSlopeField(tdomain,ydoman,formula,[(0,4),(0,3),(0,2),(0,1),(0,-1),(0,-2),(0,-3),(0,-4)])

fg.show()
