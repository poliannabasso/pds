from pds import *

#b = np.array([6, -10, 2]) #zeros da função
#a = np.array([1, -3, 2]) #polos da função
#r, p, k = sig.residuez(b, a) #calcula a expansão em frações parciais 
#print("Zeros",r,"Polos", p,"Div", k) #r - coef do dividendo; p - coef do divisor; k - resto; [z^0;z^-1;z^-2...]


b = np.array([6, -10, 2])#zeros da função
a = np.array([1, -3, 2])#polos da função
n = np.arange(-3, 5) #intervalo de tempo
x = delta(n)#impulso unitário
y = eqdif(b, a, x)
plot(n, y, 'g')
print(y[n == -1], y[n == 0], y[n == 1]) #imprime os valores de y indexados