import matplotlib.pyplot as plt

def graficar(t, y):
    plt.figure(figsize=(6, 4))
    plt.plot(t, y, label='Función')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title('Gráfico de la función')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.legend()
    plt.show()
