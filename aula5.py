from pds import *

w = np.pi/10
n = np.arange(-5,50)
x = delta(n)
plot(n, x, 'g')

b = np.array([np.sin(w)])
a = np.array([1, -2*np.cos(w), 1])
y = sig.lfilter(b, a, x)

plot(n, y, 'r')


#plotar polos
