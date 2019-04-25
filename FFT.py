import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import scipy.signal

N = 600 # number of samples
t = np.random.uniform(0.0, 1.0, N) # assuming the time start is 0.0 and time end is 1.0
S = 1.0 * np.sin(50.0 * 2 * np.pi * t) + 0.5 * np.sin(80.0 * 2 * np.pi * t)
X = S + 0.01 * np.random.randn(N) # adding noise

order = np.argsort(t)
ts = np.array(t)[order]
Xs = np.array(X)[order]

T = (t.max() - t.min()) / N # average period
Fs = 1 / T # average sample rate frequency
f = Fs * np.arange(0, N // 2 + 1) / N; # resampled frequency vector
X_new, t_new = scipy.signal.resample(Xs, N, ts)

plt.xlim(0, 0.1)
plt.plot(t_new, X_new, label="resampled")
plt.plot(ts, Xs, label="org")
plt.legend()
plt.ylabel("X")
plt.xlabel("t")

