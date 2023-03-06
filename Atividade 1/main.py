import matplotlib.pyplot as plt
import numpy as np


class Transformada2D:
    def translacao(self, pontos, tx, ty):
        matrizMultiplicacao = np.array([[1, 0, tx],
                                        [0, 1, ty],
                                        [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matrizMultiplicacao, ponto))

        return _pontos

    # Aplica a escala em relação a um conjunto de pontos
    # Distorce a figura
    def escala(self, pontos, sx, sy):
        matrizMultiplicacao = np.array([[sx, 0, 0],
                                        [0, sy, 0],
                                        [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matrizMultiplicacao, ponto))

        return _pontos

    def escalaCentroGeometrico(self, pontos, sx, sy):
        centro = self.centroGeometrico(pontos)
        _pontos = self.translacao(pontos, -centro[0], -centro[1])
        _pontos = self.escala(_pontos, sx, sy)
        _pontos = self.translacao(_pontos, centro[0], centro[1])

        return _pontos

    def escalaPonto(self, pontos, ponto, sx, sy):
        _pontos = self.translacao(pontos, -ponto[0], -ponto[1])
        _pontos = self.escala(_pontos, sx, sy)
        _pontos = self.translacao(_pontos, ponto[0], ponto[1])

        return _pontos

    def centroGeometrico(self, pontos):
        x = 0
        y = 0
        for ponto in pontos:
            x += ponto[0]
            y += ponto[1]

        return np.array([x / len(pontos), y / len(pontos)])

    def cisalhamento(self, pontos, cx, cy):
        matrizMultiplicacao = np.array([[1, cx, 0],
                                        [cy, 1, 0],
                                        [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matrizMultiplicacao, ponto))

        return _pontos

    def reflexaoEixo(self, pontos, eixo='x'):
        if eixo == 'x':
            matrizMultiplicacao = np.array([[1, 0, 0],
                                            [0, -1, 0],
                                            [0, 0, 1]], dtype=object)
        ## Y
        else:
            matrizMultiplicacao = np.array([[-1, 0, 0],
                                            [0, 1, 0],
                                            [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matrizMultiplicacao, ponto))

        return _pontos

    def reflexaoLinha(self, pontos, linha='x'):
        if linha == 'x':
            matrizMultiplicacao = np.array([[0, 1, 0],
                                            [1, 0, 0],
                                            [0, 0, 1]], dtype=object)
        ## -X
        else:
            matrizMultiplicacao = np.array([[0, -1, 0],
                                            [-1, 0, 0],
                                            [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matrizMultiplicacao, ponto))

        return _pontos


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

    transformada = Transformada2D()

    _pontos = transformada.reflexaoLinha(pontos, '-x')

    plotar(pontos[0], pontos[1], pontos[2])
    plotar(_pontos[0], _pontos[1], _pontos[2])


