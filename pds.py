import matplotlib.pyplot as plt
import numpy as np

def u(n):
    return (n>=0)*1.

def delta(n):
    return (n==0)*1.

def mse(s, r):
    return np.mean(np.abs(s-r)**2)

def plot(x, y, cor):
    plt.stem(x, y, cor)
    plt.xlabel('n')
    plt.ylabel('x [n]')
    plt.grid()
    plt.show()