import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
from scipy import constants
from scipy.integrate import odeint
#import timeit
plt.close("all")
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

hbar = 1
m = 36
k = 1.0
a = 1
U0 = 1
E = 0.1
#Define number of points for matrix
N = 1000

while True:
    E = float(input("Input a value for E between 0.1 and 0.2: "))
    if 0.1<=E<=0.2:
        U = U0-E
        def f(y,x):
            P = y[1]
            dy1dx = 72*y[0]*(U0-E-2.71828**(-x**2))
            dy2dx = P
            ## y2 = 72*y*(U0-E-e**(-x**2))
            return [dy1dx, dy2dx]
        x0 = 0
        y0 = [1,0]
        x = np.linspace(x0,100)
        sol = odeint(f, y0, x)
        #print(sol)
        break
    else:
        print("E must be between 0.1 and 0.2.")

ax1.plot(x, sol)
ax1.set_xlabel("x")
ax1.set_ylabel(r'$\psi_n$')
ax1.set_ylim(0, 10)
plt.xlim(-4, 4)
ax1.legend(loc="lower left") 
ax2.legend(loc="lower right")



plt.show()




