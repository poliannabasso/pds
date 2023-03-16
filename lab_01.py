from pds import *
# aproximacao da derivada
# h = np.array([.5,0,-.5])
h = np.array([1, -1])

######## para FIR ########
b = h
a = np.array([1])
# n = np.arange(-5,10)
# x = delta(n)
n = np.arange(-15, 15)
x = n**2

y = eqdif(b, a, x)
# resposta ao impulso
plot(n, y, 'b')


######## para IIR ########

alpha = .75
b = np.array([1])
a = np.array([1, -alpha])
n = np.arange(-5, 15)
x = delta(n)
y = eqdif(b, a, x)
plot(n, y, 'b')
