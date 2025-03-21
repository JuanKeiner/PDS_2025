import numpy as np
import matplotlib.pyplot as plt
import senoidal as s
def ejercicio2b(ti,tf,fm,fs,fi):
    t,y = s.senoidal(ti,tf,fm,fs,fi)

    yinv = -y #Esta seria una manera de invertirla

    plt.figure(figsize=(10,4))
    plt.plot(t,y,'r',label = "Senoidal")
    plt.plot(t,yinv,'b',label = 'Inversa')
    plt.grid()
    plt.show()

fs = 10
fm = 1000
fi = 0
ti = 0
tf = 5
ejercicio2b(ti,tf,fm,fs,fi)