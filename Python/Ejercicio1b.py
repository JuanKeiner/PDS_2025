import numpy as np
import matplotlib.pyplot as plt

def ejercicio1b(ti, tf, fm, fs, fi):
    T = 1/fm
    #Duracion
    t = np.linspace(ti,tf,fm)
    
    x = 2*np.pi*fs*t

    #Senoidal
    y = np.zeros(len(t))

    for i in range(len(y)):
        if x[i] != 0:
            y[i] = np.sin(x[i])/(x[i])
            print("========================================")
        else:
            y[i] = 1

    plt.figure(figsize=(10,4))
    plt.plot(t,y,label = "Senoidal Ejercicio 1b")
    plt.show()

#Ejemplo de uso
fs = 10
fm = 1000
fi = np.pi/4
ti = 0
tf = 5

ejercicio1b(ti, tf, fm, fs, fi)