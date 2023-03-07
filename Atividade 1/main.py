import matplotlib.pyplot as plt
import numpy as np
import transformada2d

def plotar(V1, V2, V3):
    plt.axis('equal')
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    plt.plot([V1[0], V2[0]], [V1[1], V2[1]], color='black')
    plt.plot([V2[0], V3[0]], [V2[1], V3[1]], color='black')
    plt.plot([V3[0], V1[0]], [V3[1], V1[1]], color='black')

    plt.show()


if __name__ == "__main__":
    pontos = [np.array([[1],
                        [1],
                        [1]], dtype=object),

              np.array([[3],
                        [5],
                        [1]], dtype=object),

              np.array([[5],
                        [1],
                        [1]], dtype=object)]

    transformada = transformada2d.Transformada2D()

    _pontos = transformada2d.rotacaoPonto(pontos, 2, 2, np.pi/2)

    plotar(pontos[0], pontos[1], pontos[2])
    plotar(_pontos[0], _pontos[1], _pontos[2])
