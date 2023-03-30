from pds import *
import sounddevice as sd

'''
Implementar um sistema de reverberação com a = 0.7 e atrasos de 50ms, 100ms e 500ms
'''

alfa = 0.7
Fs = 8192
atraso = 500*(10**-3)
x = np.load('123test.npy')
D = round(Fs*atraso)
b = np.array([1]) 
a = np.zeros(D)
a[0] = 1
a[len(a)-1] = -alfa
y = sig.lfilter(b, a, x)
sd.play(y, Fs, blocking=True)




