from pds import *

h = np.array([1,-1])
#para FIR
b = h
a = np.array([1])
n = np.arange(-5,10)
x = delta(n)
y = eqdif(b, a, x)

plot(n, y, 'b')