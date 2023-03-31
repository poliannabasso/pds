'''
Laboratório 04 - Processamento Digital de Sinais
Aluna: Polianna Beatriz Basso
RA: 2302578
Data: 30/03/2023
'''

import numpy as np
import sounddevice as sd
from scipy.io import loadmat
import matplotlib.pyplot as plt

def find_signal(time, full_sig, fragment, type='Clean'):
    #correlacao cruzada entre o sinal e o fragmento
    xCorr = np.correlate(full_sig, fragment, mode='full') 
    lags = np.arange(-len(fragment)+1, len(full_sig))
    plt.plot(lags/fs, xCorr)
    plt.grid()
    plt.xlabel('Lags (s)')
    plt.ylabel(type)
    plt.axis('tight')
    plt.show()

    #sobrepondo o fragmento no sinal
    I = np.argmax(np.abs(xCorr))
    maxt = lags[I]
    trial = np.full_like(full_sig, np.nan)
    trial[maxt+1:maxt+len(fragment)+1] = fragment
    plt.plot(time, full_sig, time, trial, 'r')
    plt.grid()
    plt.xlabel('Time (s)')
    plt.ylabel(type)
    plt.axis('tight')
    plt.show()

#sinal e fragmento recortado sem ruido
struct = loadmat('Ring.mat')
y = struct['y'][:, 0]
fs = int(struct['Fs'][0][0])
time = np.arange(0, (len(y)-1)/fs+1/fs, 1/fs)
m = min(y)
M = max(y)
full_sig = y.copy()
timeA = 7
timeB = 8
snip = np.arange(timeA*fs, timeB*fs)
fragment = full_sig[snip]
#sd.play(Full_sig, Fs, blocking=True)  # gravacao do anel girando sem ruido
#sd.play(fragment, Fs, blocking=True)  # fragmento da gravacao recortado sem ruido

mark_x = np.array([[timeA, timeB], [timeA, timeB]])
mark_y = np.array([[m, m], [M, M]])
plt.plot(time, full_sig, mark_x, mark_y, 'r--')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Clean')
plt.axis('tight')   
plt.show()
plt.plot(snip/fs, fragment)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Clean')
plt.axis('tight')   
plt.show()

find_signal(time, full_sig, fragment)

#contaminando o sinal e o fragmento recortado com ruido
noiseAmp = 0.2 * np.max(np.abs(fragment))
fragment = fragment + noiseAmp * np.random.randn(*fragment.shape)
full_sig = full_sig + noiseAmp * np.random.randn(*full_sig.shape)

#sd.play(Full_sig, Fs, blocking=True)  # gravacao do anel girando com ruido
#sd.play(fragment, Fs, blocking=True)  # fragmento da gravacao recortado com ruido
plt.plot(time, full_sig, mark_x, mark_y, 'r--')
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Noisy')
plt.axis('tight')
plt.show()

find_signal(time, full_sig, fragment, 'Noisy')
