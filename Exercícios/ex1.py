# Seja o objeto definido pelos vértices abaixo. Mostre porque se
# realizarmos uma transformação de translação e em seguida de
# escala, o resultado Rinal édiferente do que aplicarmos primeiro a
# escala e depois a translação.

# V1 = (5, 5), V2=(15, 5), V3=(10, 15)

import numpy as np
import matplotlib.pyplot as plt

def plotar(V1, V2, V3, titulo = ''):
    plt.clf()
    plt.axis([0, 50, 0, 50])
    plt.gca().set_aspect('equal', adjustable='box')

    plt.plot([V1[0], V2[0]], [V1[1], V2[1]])
    plt.plot([V2[0], V3[0]], [V2[1], V3[1]])
    plt.plot([V3[0], V1[0]], [V3[1], V1[1]])

    plt.title(titulo)
    plt.show()

def translacao(V1, V2, V3, tX, tY):
    V1 = V1 + np.array([tX, tY])
    V2 = V2 + np.array([tX, tY])
    V3 = V3 + np.array([tX, tY])

    return V1, V2, V3

def escala(V1, V2, V3, escala):
    V1 = V1*escala
    V2 = V2*escala
    V3 = V3*escala

    return V1, V2, V3



if __name__ == '__main__':

    V1 = np.array([5, 5])
    V2 = np.array([15, 5])
    V3 = np.array([10, 15])
    plotar(V1, V2, V3)

    V1TE, V2TE, V3TE = translacao(V1, V2, V3, 10, 10)
    V1TE, V2TE, V3TE = escala(V1TE, V2TE, V3TE, 2)

    V1ET, V2ET, V3ET = escala(V1, V2, V3, 2)
    V1ET, V2ET, V3ET = translacao(V1ET, V2ET, V3ET, 10, 10)

    plotar(V1TE, V2TE, V3TE, 'Translação e Escala')
    plotar(V1ET, V2ET, V3ET, 'Escala e Translação')







