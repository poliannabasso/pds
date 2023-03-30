import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

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
    for n in range(x.size):
        for k in range(1, min(len(a), n+1)):
            y[n] -= a[k]*y[n-k]
        for k in range(0, min(len(b), n+1)):
            y[n] += b[k]*x[n-k]
    return y

def media_movel(x, M):
    b = np.ones(M+1)
    for m in range(0, b.size):
        b[m] = (1/(m+1))
    y = eqdif(b, [1], x)
    return y
