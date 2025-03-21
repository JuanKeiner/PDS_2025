import numpy as np
import matplotlib.pyplot as plt
import senoidal as s
def ejercicio2c(ti,tf,fm,fs,fi):
    t,y = s.senoidal(ti,tf,fm,fs,fi)
    N = 8 #Cantidad de escalones
    max = np.max(y)
    min = np.min(y)
    dif = np.abs(max - min)
    H = dif/(N-1)

    if min < 0:
        y = y-min

    p = np.zeros(len(t))
    #Cuantizo de acuerdo a la formula del libro
    for i in range(len(t)):
        if y[i] < 0:
            p[i] = 0
        elif y[i] >= 0 and y[i] < (N - 1)*H:
            p[i] = H*np.round(y[i]/H)
        else:
            p[i] = (N - 1)*H

    plt.figure(figsize=(10,4))
    plt.plot(t,y,'r',label = "Senoidal")
    plt.plot(t,p,'b',label = 'Inversa')
    plt.grid()
    plt.show()

fs = 2
fm = 200
fi = 0
ti = 0
tf = 1
ejercicio2c(ti,tf,fm,fs,fi)