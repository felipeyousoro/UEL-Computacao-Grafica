import matplotlib.pyplot as plt
import numpy as np
import transformada2d

def plotar(V1, V2, V3, V4, title=''):
    plt.axis([-5, 10, -5, 10])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')

    plt.plot([V1[0], V2[0]], [V1[1], V2[1]], color='black')
    plt.plot([V2[0], V3[0]], [V2[1], V3[1]], color='black')
    plt.plot([V3[0], V4[0]], [V3[1], V4[1]], color='black')
    plt.plot([V4[0], V1[0]], [V4[1], V1[1]], color='black')

    plt.title(title)
    plt.show()


if __name__ == "__main__":
    pontos = [np.array([[1],
                        [1],
                        [1]], dtype=object),

              np.array([[1],
                        [3],
                        [1]], dtype=object),

              np.array([[3],
                        [3],
                        [1]], dtype=object),

              np.array([[3],
                        [1],
                        [1]], dtype=object)]

    transformada = transformada2d.Transformada2D()


    plotar(pontos[0], pontos[1], pontos[2], pontos[3], 'Original')

    _pontos = transformada.translacao(pontos, 2, 2)
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Transladado em (2, 2)')

    _pontos = transformada.escala(pontos, 2, 2)
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Escala 2x, 2y sem transladar')

    _pontos = transformada.escalaCentroGeometrico(pontos, 2, 2)
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Escala 2x, 2y em torno do centro geométrico')

    _pontos = transformada.escalaPonto(pontos, 2, 2, 5, 5)
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Escala 2x, 2y em torno do ponto (5, 5)')

    _pontos = transformada.rotacao(pontos, np.pi/2)
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Rotacionado 90º sem transladar')

    _pontos = transformada.rotacaoPonto(pontos, 2, 2, np.pi/4)
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Rotacionado 45º em torno do ponto (5, 5)')

    _pontos = transformada.rotacaoPonto(pontos, pontos[0][0], pontos[0][1], np.pi / 4)
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Rotacionado 45º em torno do ponto (1, 1)')

    _pontos = transformada.cisalhamento(pontos, 2, 0)
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Cisalhamento 2x')

    _pontos = transformada.reflexaoEixo(pontos, 'x')
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Reflexão no eixo x')

    _pontos = transformada.reflexaoLinha(pontos, '-x')
    plotar(_pontos[0], _pontos[1], _pontos[2], _pontos[3], 'Reflexão na linha y = -x')
