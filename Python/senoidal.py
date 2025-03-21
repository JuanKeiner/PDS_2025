import numpy as np
def senoidal(ti, tf, fm, fs, fi):
    T = 1/fm
    t = np.linspace(ti,tf - T,(tf - ti)*fm)       #en linspace tengo que ponerle fm porque es la frecuencia de muestreo
    y = np.sin(2*np.pi*fs*t + fi)
    return t,y