from pds import *

n = np.arange(-15,15)
x = n**2
y = x[1:]-x[:-1]

plt.stem(n[1:], y, 'k')
plt.stem(n[:-1], y, 'r')
plt.stem(n, 2*n, 'g')

plt.grid()
plt.show()