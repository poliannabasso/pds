import numpy as np
import sounddevice as sd
from scipy.io import loadmat
import matplotlib.pyplot as plt

struct = loadmat('Ring.mat')
y = struct['y'][:, 0]
Fs = int(struct['Fs'][0][0])

time = np.arange(0, (len(y)-1)/Fs+1/Fs, 1/Fs)
m = min(y)
M = max(y)
Full_sig = y.copy()
timeA = 7
timeB = 8
snip = np.arange(timeA*Fs, timeB*Fs)

fragment = Full_sig[snip]
#sd.play(y, Fs, blocking=True)

mark_x = np.array([[timeA, timeB], [timeA, timeB]])
mark_y = np.array([[m, m], [M, M]])
#plt.plot(time, Full_sig, mark_x, mark_y, 'r--')
#plt.grid()
#plt.show()
#plt.plot(snip/Fs, fragment)
#plt.grid()
#plt.show()
#sd.play(fragment, Fs, blocking=True)

#######################################################

xCorr, lags = np.correlate(Full_sig, fragment, mode='full'), np.arange(-len(fragment)+1, len(Full_sig))

plt.plot(lags/Fs, xCorr)
plt.grid()
plt.show()

#######################################################

xCorr, lags = np.correlate(Full_sig, fragment, mode='full'), np.arange(-len(fragment)+1, len(Full_sig))
I = np.argmax(np.abs(xCorr))
maxt = lags[I]

Trial = np.full_like(Full_sig, np.nan)
Trial[maxt+1:maxt+len(fragment)+1] = fragment

plt.plot(time, Full_sig, time, Trial)
plt.show()

#######################################################

NoiseAmp = 0.2*np.max(np.abs(fragment))
fragment = fragment + NoiseAmp*np.random.randn(len(fragment))
Full_sig = Full_sig + NoiseAmp*np.random.randn(len(Full_sig))

plt.plot(time, Full_sig, [timeA, timeB], [m, m], 'r--', [timeA, timeB], [M, M], 'r--')
plt.xlabel('Time (s)')
plt.ylabel('Noisy')
plt.axis('tight')
plt.show()

#######################################################

xCorr, lags = np.correlate(Full_sig, fragment, mode='full'), np.arange(-len(fragment)+1, len(Full_sig))

plt.plot(lags/Fs, xCorr)
plt.grid()
plt.show()

#######################################################

xCorr, lags = np.correlate(Full_sig, fragment, mode='full'), np.arange(-len(fragment)+1, len(Full_sig))
I = np.argmax(np.abs(xCorr))
maxt = lags[I]

Trial = np.full_like(Full_sig, np.nan)
Trial[maxt+1:maxt+len(fragment)+1] = fragment

plt.figure()
plt.plot(time, Full_sig, time, Trial)
plt.show()