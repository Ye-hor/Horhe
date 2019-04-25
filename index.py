import pyedflib
import FileController as fc
import matplotlib.pyplot as plt
import numpy as np
import scipy
dataFromFile = fc.GetSignalsListFromEDFPRO("Akubenko_AB_01.edf")

fs = 500
t = np.arange(0, 1, fs)       # Time vector

x = np.arange(dataFromFile.shape[1])

y1 = np.multiply(np.array(dataFromFile[11]),1e-3)

line = plt.plot(t[len(x)], y1)
plt.setp(line, color='grey', linewidth=1.0)
legend = plt.legend(loc='best', shadow=True, fontsize='large')
plt.xlabel('x',fontsize='large')
plt.ylabel('y',fontsize='large')
plt.grid(True)
plt.show()

spectrum = np.fft.fft(y1)
s=np.abs(spectrum[0:round(len(spectrum)/2)])
f=np.fft.fftfreq(len(spectrum), 1/fs)
plt.plot(f[0:round(len(spectrum)/2)], s)
plt.show()