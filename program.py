import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt
from scipy import constants
from scipy.integrate import odeint
from scipy.special import erf
plt.close("all")
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

hbar = 1
m = 36
a = 1
U0 = 1
E = 0.1


while True:
    E = float(input("Input a value for E between 0.1 and 0.2: "))
    if 0.1<=E<=0.2:
        U = U0-E
        def f(y,x):
            P = y[1]
            dy1dx = 72*y[0]*(U-(2.71828**(-x**2)))
            dy2dx = P
            return [dy1dx, dy2dx]
        x0 = 0
        y0 = [1,.0002]
        x = np.linspace(-4,4)
        w = np.linspace(-4,4)
        sol = odeint(f, y0, x)
        # print(sol)
        break
    else:
        print("E must be between 0.1 and 0.2.")

Pot = (1-(2.71828**(-w**2)))
plt.plot(w, Pot)       
plt.plot(x, sol)
plt.xlabel("x")
plt.ylabel(r'$\psi_n$')
plt.xlim(-4, 4)
plt.ylim(-1,1.1)

plt.title("Wavefunction Plot")


plt.show()

plt.show()





