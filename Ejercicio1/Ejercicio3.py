import numpy as np
import matplotlib.pyplot as plt

def cuadrada(tini, tfin, fm, fs,fase):
    T = 1/fm

    t = np.linspace(tini, tfin-T, fm)
    
    mod = np.mod(2*np.pi*fs*t+fase,2*np.pi)

    cuadrada = np.where(mod >= np.pi, -1, 1)

    return t,cuadrada

tini = 0
tfin = 5
fm = 50
fs =  20
fase = 0

t,seno = cuadrada(tini,tfin,fm,fs,fase)

plt.figure()
plt.plot(t,seno)
plt.stem(t,seno)
plt.grid()
plt.show()

