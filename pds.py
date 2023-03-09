import matplotlib.pyplot as plt
import numpy as np


def u(n):
    return (n >= 0)*1.


def delta(n):
    return (n == 0)*1.


def mse(s, r):
    return np.mean(np.abs(s-r)**2)


def plot(x, y, cor):
    plt.stem(x, y, cor)
    plt.xlabel('n')
    plt.ylabel('x [n]')
    plt.grid()
    plt.show()

# na pratica o tamanho de x pode ser infinito
# os coeficientes do filtro (a e b) são finitos
def eqdif(b, a, x):
    y = np.zeros_like(x)
    for n in range(0, len(y)):
        for k in range(1, len(a)):
            if n-k>=0:
                y[n] -= a[k]*y[n-k]
        for k in range(len(b)):
            if n-k>=0:
               y[n] += b[k]*x[n-k]
    return y
