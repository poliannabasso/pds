from pds import *

F = 100
Fs = 1000
T = 1/Fs

xc = lambda t: np.cos(2*np.pi*F*t)
n = np.arange(-10,31)
x = xc(n*T)
plot(n, x, 'g')

f = F/Fs
print(f)
w0 = 2*np.pi*f
print(w0)