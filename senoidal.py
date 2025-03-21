import numpy as np

def senoidal(tini, tfin, fm, fs, fase):
    T = 1/fm

    t = np.linspace(tini, tfin-T, fm)

    print(2*np.pi*fm*t)
    
    seno = np.sin(2*np.pi*fs*t + fase)

    return t,seno