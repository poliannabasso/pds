from pds import *

n = np.arange(40)
s = np.exp(-0.2*n)*np.cos(0.3*np.pi*n)*u(n)
r = np.exp(-0.00000000001*n)*np.cos(0.1*np.pi*n)*u(n)

plot(n, r, 'y')
plot(n, s, 'g')
