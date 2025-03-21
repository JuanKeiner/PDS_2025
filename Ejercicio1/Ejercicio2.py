import numpy as np
import matplotlib.pyplot as plt

def sync(tini, tfin, fm, fase):
    T = 1/fm

    t = np.linspace(tini, tfin-T, fm)
    
    x = 2*np.pi*fs*t + fase

    sinc = np.where(x!=0,np.sin(x)/x,1)

    return t,sinc

tini = -5
tfin = 5
fm = 100
fs = 1
fase = 0

t,seno = sync(tini,tfin,fm,fase)

plt.figure()
plt.plot(t,seno)
plt.stem(t,seno)
plt.grid()
plt.show()

