from pds import *

'''
Laboratório 02 - Polianna Basso
Filtragem de senoides contaminadas com ruído 
utilizando filtros de média móvel.

1.Gerar uma senóide com w0 = pi/10 e -30 <= n <30
2.Contaminar a senóide com ruído AWGN (additive white Gaussian noise)
sigma = 0.1; 0.5; 1;
3.Filtrar com filtro de média móvel M = 2,5,10; (usar função eqdif)
4.Plotar sinais antes e depois 
'''

n = np.arange(-30, 30)
w0 = np.pi/10
x_clean = np.cos(w0*n)
sigma = 0.5
x = x_clean + np.random.randn(n.size)*sigma

plot(n, x_clean, 'g')
plot(n, x, 'y')
M = np.array([2, 5, 10])

y1 = media_movel(x, M[0])
plot(n, y1, 'r')
y2 = media_movel(x, M[1])
plot(n, y2, 'b')
y3 = media_movel(x, M[2])
plot(n, y3, 'g')
