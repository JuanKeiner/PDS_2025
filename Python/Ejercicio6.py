import numpy as np
import matplotlib.pyplot as plt
import senoidal as s
import interpoladores as inter
#Resolucion del ejercicio 6 de la guia numero 1
#Datos para calcular la senoidal

ti = 0
tf = 3
fs = 0.5
fm = 10
fi = 0

#Periodo original
T = 1/fm

#Sobremuestra -> Se multiplica por 4 la cantidad de muestras
n = 4

#Periodo nuevo
T_i = T/n

#Obtengo la senoidal original
to,yo = s.senoidal(ti,tf,fm,fs,fi)

#Tiempo discreto nuevo
tn = np.arange(ti,tf - T_i, T_i) #n*fm es la nueva frecuencia de muestro

m = np.size(tn) #Tama�o del tiempo nuevo
n = np.size(to) #Tama�o del tiempo original
xi_sinc = np.zeros(m) #Se�al sobremuestreada pero vacia
xi_escalon = np.zeros(m)
xi_lineal = np.zeros(m)

for i in range(len(tn)):
    for j in range(len(to)):
        indice = (tn[i] - to[j])/T

        #Interpolador sinc.
        xi_sinc[i] += yo[j]*inter.sinc(fs,indice)

        #Interpolador escalon.
        xi_escalon[i] += yo[j]*inter.escalon(indice)

        #Interpolador lineal.
        xi_lineal[i] += yo[j]*inter.lineal(indice)

plt.figure(figsize=(10,4))
plt.plot(to,yo,'r-*',label = "Original")
plt.stem(tn,xi_sinc,'b-o',label = 'Interpolador')
plt.grid()
plt.show()

plt.figure(2,figsize=(10,4))
plt.plot(to,yo,'r-*',label = "Original")
plt.stem(tn,xi_escalon,'b-o',label = 'Interpolador')
plt.grid()
plt.show()

plt.figure(3,figsize=(10,4))
plt.plot(to,yo,'r-*',label = "Original")
plt.stem(tn,xi_lineal,'b-o',label = 'Interpolador')
plt.grid()
plt.show()