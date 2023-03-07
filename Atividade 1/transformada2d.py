import numpy as np


class Transformada2D:
    def translacao(self, pontos, tx, ty):
        matriz_translacao = np.array([[1, 0, tx],
                                      [0, 1, ty],
                                      [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matriz_translacao, ponto))

        return _pontos

    def escala(self, pontos, sx, sy):
        matriz_escala = np.array([[sx, 0, 0],
                                  [0, sy, 0],
                                  [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matriz_escala, ponto))

        return _pontos

    def escalaCentroGeometrico(self, pontos, sx, sy):
        centro = self.getCentroGeometrico(pontos)

        matriz_translacao = np.array([[1, 0, centro[0]],
                                      [0, 1, centro[1]],
                                      [0, 0, 1]], dtype=object)

        matriz_escala = np.array([[sx, 0, 0],
                                  [0, sy, 0],
                                  [0, 0, 1]], dtype=object)

        matriz_translacao_inversa = np.array([[1, 0, -centro[0]],
                                              [0, 1, -centro[1]],
                                              [0, 0, 1]], dtype=object)

        matriz_composta = np.dot(matriz_translacao, np.dot(matriz_escala, matriz_translacao_inversa))

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matriz_composta, ponto))

        return _pontos

    def escalaPonto(self, pontos, x, y, sx, sy):
        matriz_translacao = np.array([[1, 0, x],
                                      [0, 1, y],
                                      [0, 0, 1]], dtype=object)

        matriz_escala = np.array([[sx, 0, 0],
                                  [0, sy, 0],
                                  [0, 0, 1]], dtype=object)

        matriz_translacao_inversa = np.array([[1, 0, -x],
                                              [0, 1, -y],
                                              [0, 0, 1]], dtype=object)

        matriz_composta = np.dot(matriz_translacao, np.dot(matriz_escala, matriz_translacao_inversa))

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matriz_composta, ponto))

        return _pontos

    def getCentroGeometrico(self, pontos):
        x = 0
        y = 0
        for ponto in pontos:
            x += ponto[0]
            y += ponto[1]

        return np.array([x / len(pontos), y / len(pontos)])

    def rotacao(self, pontos, angulo):
        matriz_rotacao = np.array([[np.cos(angulo), -np.sin(angulo), 0],
                                   [np.sin(angulo), np.cos(angulo), 0],
                                   [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matriz_rotacao, ponto))

        return _pontos

    def rotacaoPonto(self, pontos, x, y, angulo):
        matriz_translacao = np.array([[1, 0, x],
                                      [0, 1, y],
                                      [0, 0, 1]], dtype=object)

        matriz_rotacao = np.array([[np.cos(angulo), -np.sin(angulo), 0],
                                   [np.sin(angulo), np.cos(angulo), 0],
                                   [0, 0, 1]], dtype=object)

        matriz_translacao_inversa = np.array([[1, 0, -x],
                                              [0, 1, -y],
                                              [0, 0, 1]], dtype=object)

        matriz_composta = np.dot(matriz_translacao, np.dot(matriz_rotacao, matriz_translacao_inversa))

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matriz_composta, ponto))

        return _pontos

    def cisalhamento(self, pontos, cx, cy):
        matriz_cisalhamento = np.array([[1, cx, 0],
                                        [cy, 1, 0],
                                        [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matriz_cisalhamento, ponto))

        return _pontos

    def reflexaoEixo(self, pontos, eixo='x'):
        if eixo == 'x':
            matriz_reflexao = np.array([[1, 0, 0],
                                        [0, -1, 0],
                                        [0, 0, 1]], dtype=object)
        ## Y
        else:
            matriz_reflexao = np.array([[-1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matriz_reflexao, ponto))

        return _pontos

    def reflexaoLinha(self, pontos, linha='x'):
        if linha == 'x':
            matriz_reflexao = np.array([[0, 1, 0],
                                        [1, 0, 0],
                                        [0, 0, 1]], dtype=object)
        ## -X
        else:
            matriz_reflexao = np.array([[0, -1, 0],
                                        [-1, 0, 0],
                                        [0, 0, 1]], dtype=object)

        _pontos = []
        for ponto in pontos:
            _pontos.append(np.dot(matriz_reflexao, ponto))

        return _pontos
