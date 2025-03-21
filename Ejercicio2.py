import senoidal as sin
import numpy as np
import matplotlib.pyplot as plt

#===================INVERSION===================
tini = 0
tfin = 1
fm = 100
fs = 4
fase = 0

t,seno = sin.senoidal(tini,tfin,fm,fs,fase)

plt.figure(1)
plt.plot(t,seno)
plt.plot(-t,seno)
plt.grid()
plt.legend(["Original", "Invertida"]) #Para las legend tiene que ser un vector
plt.title("Inversion")
plt.show(block = False)

#===================RECTIFICACION===================

#La rectificacion de media onda solo conserva la parte positiva de la señal y el resto es cero.
media_onda = []
for valor in seno:
    if valor < 0:
        media_onda.append(0)
    else:
        media_onda.append(valor)
#La rectificacion de onda completa invierte los valores negativos de la señal haciendo que toda 
#la señal sea positiva
onda_completa = []
for valor in seno: 
    if valor < 0:
        onda_completa.append(np.abs(valor))
    else:
        onda_completa.append(valor)

plt.figure(2)
plt.plot(t,media_onda)
plt.plot(t,onda_completa)
plt.title("Rectificacion")
plt.legend(["Media onda", "Onda completa"]) #Para las legend tiene que ser un vector
plt.grid()
plt.show(block = False)

#===================CUANTIZACION===================

tini = 0
tfin = 1
fm = 100
fs = 2
fase = 0

t,sin = sin.senoidal(tini,tfin,fm,fs,fase)

N = 8 #Cantidad de escalones.
max = np.max(sin)
min = np.min(sin)
dif = np.abs(max - min)
H = dif/(N-1)
if min < 0: 
    y = sin - min

cuant = np.zeros(len(t))

#Cuantizo de acuerdo a la formula del libro
for i in range(len(t)):
    if y[i] < 0:
        cuant[i] = 0
    elif y[i] > 0 and y[i]<(N-1)*H:
        cuant[i] = H*np.round(y[i]/H)
    else:
        cuant[i] = (N - 1)*H

plt.figure(3)
plt.plot(t,sin,'r',label="Senoidal")
plt.plot(t,cuant,'b',label = "Cuantizada")
plt.grid()
plt.show()
