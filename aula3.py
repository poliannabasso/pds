from pds import *

n = np.arange(-10,31)
w1 = np.pi/10
w2 = np.pi/10 + 2*np.pi
w3 = np.pi/10 + 2*np.pi*4
x1 = np.cos(w1*n)
x2 = np.cos(w2*n)
x3 = np.cos(w3*n)

plot(n,x1, 'g')
plot(n,x2, 'y')
plot(n,x3, 'b')

print(mse(x1, x2))