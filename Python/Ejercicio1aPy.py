import numpy as np
import matplotlib.pyplot as plt

def senoidal(ti, tf, fm, fs, fase):
    
    #Durecion
    t = tf - ti
    tiempo = np.linspace(ti,tf,fm)

    #Senoidal discreta
    y = np.sin(2*np.pi * fm * tiempo + fase)

    return tiempo, y

#Ejemplo de uso
fs = 10      #Frecuencia de muestreo
fm = 1000         #Frecuencia de la senoidal
fase = np.pi/4  #Fase de la senoidal en radianes
ti = 0
tf = 1

tiempo,y = senoidal(ti,tf,fm,fs,fase)

plt.figure(figsize=(10,4))
plt.plot(tiempo,y,label = "Senoidal")
plt.show()