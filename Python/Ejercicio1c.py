#Resolucion del ejercicio 1.3 guia 1
import numpy as np
import matplotlib.pyplot as plt

def ejercicio1c(ti, tf, fm, fs, fi):
    T = 1/fm
    t = np.linspace(ti,tf,fm)

    print(t)

    #Obtengo el vector funcion
    y = np.zeros(len(t))

    print(len(t))

    for i in range(len(t)):
        print(t[i])
        if np.mod(2*np.pi*fs*t[i] + fi,2*np.pi) >= np.pi:
            #print("Entro pues -> ",np.mod(2*np.pi*fs*t[i],2*np.pi))
            y[i] = -1
        else:
            y[i] = 1

    print(np.size(y))

    plt.figure(figsize=(10,4))
    plt.plot(t,y,'r-o',label = "Senoidal Ejercicio 1b")
    plt.show()

#Ejemplo de uso
fs = 10
fm = 100
fi = 0
ti = 0
tf = 1

ejercicio1c(ti, tf, fm, fs, fi)