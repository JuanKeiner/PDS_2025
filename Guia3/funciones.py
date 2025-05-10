import numpy as np
import matplotlib.pyplot as plt

def señal_senoidal(tiempo_inicial, tiempo_final, frecuencia_senoidal, frecuencia_muestreo, fase):
    Ts = 1 / frecuencia_muestreo  # Período de muestreo
    tiempo = np.arange(tiempo_inicial, tiempo_final, Ts)  # Instantes de muestreo
    y = np.sin(2 * np.pi * frecuencia_senoidal * tiempo + fase)  # Señal muestreada
    return tiempo, y

def señal_rampa(longitud, amplitud, frecuencia_muestreo):
    Ts = 1 / frecuencia_muestreo  # Período de muestreo
    tiempo = np.arange(0, longitud, Ts)  # Instantes de muestreo
    y = tiempo * (amplitud/longitud)  # Señal rampa
    return tiempo, y

def señal_cuadrada(longitud, amplitud, frecuencia_periodo, frecuencia_muestreo):
    Ts = 1 / frecuencia_muestreo  # Período de muestreo
    tiempo = np.arange(0, longitud, Ts)  # Instantes de muestreo
    y = np.where((tiempo % frecuencia_periodo) < (frecuencia_periodo / 2), -amplitud, amplitud)
    return tiempo, y