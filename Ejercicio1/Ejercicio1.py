import numpy as np
import matplotlib.pyplot as plt

def senoidal(tini, tfin, fm, fs, fase):
    T = 1/fm

    t = np.linspace(tini, tfin-T, fm)
    
    seno = np.sin(2*np.pi*fs*t + fase)

    return t,seno

tini = 0
tfin = 1
fm = 50
fs = 2
fase = 0

t,seno = senoidal(tini,tfin,fm,fs,fase)

plt.figure()
plt.stem(t,seno)
plt.plot(t,seno)
plt.show()

