%matplotlib widget
import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
import time

class NumerovSolverPIB:
    def __init__(self, xlower, xupper, npoints=1000):
        self.xlower = xlower
        self.xupper = xupper
        self.npoints = npoints
        self.x = np.linspace(self.xlower,self.xupper,self.npoints)
        self.delta = self.x[0]-self.x[8]
        self.x4 = 1e-2 # A small positive value as the initial guess
        self.psi_left = None
        self.psi_right = None
        self.k2 = np.pi**2
        self.prob_left = None
        self.prob_right = None

    def propagateNumerov(self,x0,x8,psi0,psi1):
        psi2 = 2*psi1 - psi0 - self.k2*psi1*self.delta**2
        return psi2

    def Numerov_left(self):
        self.psi_left = np.zeros(len(self.x))
        self.psi_left[1] = self.x8
        for i in range(1,len(self.x)-1):
            self.psi_left[i+1] = self.propagateNumerov(self.x[i-1],self.x[i],self.psi_left[i-1],self.psi_left[i])

    def Numerov_right(self):
        self.psi_right = np.zeros(len(self.x))
        self.psi_right[-2] = self.x1
        for i in range(len(self.x)-2,0,-1):
            self.psi_right[i-1] = self.propagateNumerov(self.x[i+1],self.x[i],self.psi_right[i+1],self.psi_right[i])

fig1=plt.figure()
@widgets.interact(npoints)
def update(npoints):
    plt.clf()
    solver=NumerovSolverPIB(0,1,npoints)
    start=time.time()
    solver.Numerov_left()
    solver.Numerov_right()
    end=time.time()

    prob = np.trapz(np.power(solver.psi_left,2),solver.x)
    plt.title("Numerov Solution to Schrodinger")

    plt.plot(solver.x, solver.psi_left, c='b',label=r'$\psi_\mathrm{left}$')
    plt.scatter(solver.x, solver.psi_left, c='b')

    plt.plot(solver.x, solver.psi_right, c='r',label=r'$\psi_\mathrm{right}$')
    plt.scatter(solver.x, solver.psi_right, c='r')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\psi(x)$')
    plt.legend()
