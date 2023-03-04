# Quais são as transformações geométricas necessárias para que o
# objeto fique como especificado na figura B a partir da figura A?
# Especifique o tipo e os respectivos fatores de transformação.

# Tá errado mas chega bem perto

import numpy as np
import matplotlib.pyplot as plt

def plotar(V1, V2, V3, V4, titulo=''):
    plt.clf()
    plt.axis([0, 10, 0, 10])
    plt.gca().set_aspect('equal', adjustable='box')

    plt.plot([V1[0], V2[0]], [V1[1], V2[1]])
    plt.plot([V1[0], V3[0]], [V1[1], V3[1]])
    plt.plot([V2[0], V4[0]], [V2[1], V4[1]])
    plt.plot([V3[0], V4[0]], [V3[1], V4[1]])

    plt.title(titulo)
    plt.show()


def transladarParaPonto(pontos, ponto):
    p1 = pontos[0]

    _pontos = []
    for i in range(len(pontos)):
        _pontos.append(pontos[i] - p1 + ponto)

    return _pontos


def escalar(pontos, escala):
    _pontos = []
    for ponto in pontos:
        _pontos.append(ponto * escala)

    return _pontos


def calcularAngulo(V1):  # em radianos
    angulo = np.arctan2(V1[1], V1[0])
    return angulo


def rotacionarPonto(ponto, angulo):
    x = ponto[0] * np.cos(angulo) - ponto[1] * np.sin(angulo)
    y = ponto[0] * np.sin(angulo) + ponto[1] * np.cos(angulo)

    return np.array([x, y])

def rotacionar(pontos, angulo):
    _pontos = transladarParaPonto(pontos, [0, 0])
    _pontos = list(_pontos)

    for i in range(len(_pontos)):
        _pontos[i] = rotacionarPonto(_pontos[i], angulo)

    return _pontos

def escalar(pontos, escala):
    _pontos = []
    for ponto in pontos:
        _pontos.append(ponto * escala)

    return _pontos

if __name__ == '__main__':
    V1 = np.array([1, 1])
    V2 = np.array([1, 3])
    V3 = np.array([3, 1])
    V4 = np.array([3, 3])

    _pontos = rotacionar([V1, V2, V3, V4], np.pi/4)
    _pontos = escalar(_pontos, 2)
    _pontos = transladarParaPonto(_pontos, [3, 0])
    print(_pontos)
    print(_pontos)
    print(V1)
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Resultado')