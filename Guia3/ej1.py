
import funciones
import utiles

def main():
    tSenoidal, ySenoidal = funciones.señal_senoidal(0,10,0.5,10,0)
    tRampa, yRampa = funciones.señal_rampa(10,1,10)
    tCuadrada, yCuadrada = funciones.señal_cuadrada(10,1,2,10)
    # tAleatoria, yAleatoria = funciones.señalAleatoria()

    utiles.graficar(tSenoidal, ySenoidal)
    utiles.graficar(tRampa, yRampa)
    utiles.graficar(tCuadrada, yCuadrada)