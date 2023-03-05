# Rotacione o triângulo da figura em 90° (sentido anti-horário) em
# relação ao ponto P = (6,5)
# os vértices do triângulo em coordenadas homogêneas estão relacionados
# abaixo:

import numpy as np
import matplotlib.pyplot as plt


def transladar(pontos, tx, ty):
    T = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    _pontos = []

    for p in pontos:
        _pontos.append(np.dot(T, p))

    return _pontos


def plotar(V1, V2, V3, pontoP):
    plt.clf()
    plt.axis([0, 10, 0, 10])
    plt.gca().set_aspect('equal', adjustable='box')

    plt.plot([V1[0], V2[0]], [V1[1], V2[1]])
    plt.plot([V1[0], V3[0]], [V1[1], V3[1]])
    plt.plot([V2[0], V3[0]], [V2[1], V3[1]])
    plt.plot(pontoP[0], pontoP[1], 'ro')

    plt.show()


def rotacionarPontoHomogeneo(ponto, angulo):
    matrizRotacao = np.array([[np.cos(angulo), -np.sin(angulo), 0],
                              [np.sin(angulo), np.cos(angulo), 0],
                              [0, 0, 1]])

    return np.dot(matrizRotacao, ponto)


def rotacionarHomogeneo(pontos, angulo):
    _pontos = list(pontos)

    for i in range(len(_pontos)):
        _pontos[i] = rotacionarPontoHomogeneo(_pontos[i], angulo)

    return _pontos


if __name__ == '__main__':
    # [X, Y, 1]
    A = np.array([[3], [2], [1]])
    B = np.array([[9], [2], [1]])
    C = np.array([[7], [10], [1]])

    P = np.array([6, 5])

    pontos = [A, B, C]
    plotar(pontos[0], pontos[1], pontos[2], P)

    pontos = transladar(pontos, -P[0], -P[1])
    plotar(pontos[0], pontos[1], pontos[2], P)

    pontos = rotacionarHomogeneo(pontos, np.pi / 2)
    plotar(pontos[0], pontos[1], pontos[2], P)

    pontos = transladar(pontos, P[0], P[1])
    plotar(pontos[0], pontos[1], pontos[2], P)