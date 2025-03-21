import numpy as np

#Interpolador sinc
def sinc(fs,indice):
    x = 2*np.pi*fs*indice
    t = 0
    if x == 0:
        t = 1
    else:
        t = np.sin(x) / x
    return t

#Interpolador lineal
def lineal(indice):
    t = 0
    if np.abs(indice) < 1:
        t = 1 - np.abs(indice)
    return t

#Interpolador escalon
def escalon(indice):
    if (indice >= 1e-12 and indice <= 1):
        t = 1
    else:
        t = 0
    return t
