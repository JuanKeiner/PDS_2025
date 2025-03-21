import numpy as np
import matplotlib.pyplot as plt
import senoidal as s
#Resolucion del 2a -> inversion
def ejercicio2a(tf,ti,fm,fs,fi):
    
    #Funcion que calcula la senoidal
    t,y = s.senoidal(tf,ti,fm,fs,fi)

    yrec1 = np.zeros(len(y))
    yrec2 = np.zeros(len(y))

    #Calculo de la inversion
    for i in range(len(t)):
        if y[i] < 0:
            yrec1[i] = 0
            yrec2[i] = -y[i]
        else:
            yrec1[i] = y[i]
            yrec2[i] = y[i]

    plt.figure(figsize=(10,4))
    plt.plot(t,y,'r',label = "Senoidal")
    plt.plot(t,yrec1,'b',label = 'Rect. Onda Media')
    plt.plot(t,yrec2,'g',label = 'Rect. Onda Completa')
    plt.grid()
    plt.show()


fs = 10
fm = 1000
fi = 0
ti = 0
tf = 5
ejercicio2a(ti,tf,fm,fs,fi)