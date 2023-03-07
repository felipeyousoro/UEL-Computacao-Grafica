import numpy as np


class Transformada2D:
    def translacao(self, ponto, tx, ty):
        matriz_translacao = np.array([[1, 0, tx],
                                      [0, 1, ty],
                                      [0, 0, 1]], dtype=object)

        return np.dot(matriz_translacao, ponto)

    def escala(self, ponto, sx, sy):
        matriz_escala = np.array([[sx, 0, 0],
                                  [0, sy, 0],
                                  [0, 0, 1]], dtype=object)

        return np.dot(matriz_escala, ponto)

    def escalaCentroGeometrico(self, ponto, centro, sx, sy):
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

        return np.dot(matriz_composta, ponto)

    def escalaPonto(self, ponto, referencia, sx, sy):
        matriz_translacao = np.array([[1, 0, referencia[0]],
                                      [0, 1, referencia[1]],
                                      [0, 0, 1]], dtype=object)

        matriz_escala = np.array([[sx, 0, 0],
                                  [0, sy, 0],
                                  [0, 0, 1]], dtype=object)

        matriz_translacao_inversa = np.array([[1, 0, -x],
                                              [0, 1, -y],
                                              [0, 0, 1]], dtype=object)

        matriz_composta = np.dot(matriz_translacao, np.dot(matriz_escala, matriz_translacao_inversa))

        return np.dot(matriz_composta, ponto)

    def rotacao(self, ponto, angulo):
        matriz_rotacao = np.array([[np.cos(angulo), -np.sin(angulo), 0],
                                   [np.sin(angulo), np.cos(angulo), 0],
                                   [0, 0, 1]], dtype=object)

        return np.dot(matriz_rotacao, ponto)

    def rotacaoPonto(self, ponto, referencia, angulo):
        matriz_translacao = np.array([[1, 0, referencia[0]],
                                      [0, 1, referencia[1]],
                                      [0, 0, 1]], dtype=object)

        matriz_rotacao = np.array([[np.cos(angulo), -np.sin(angulo), 0],
                                   [np.sin(angulo), np.cos(angulo), 0],
                                   [0, 0, 1]], dtype=object)

        matriz_translacao_inversa = np.array([[1, 0, -x],
                                              [0, 1, -y],
                                              [0, 0, 1]], dtype=object)

        matriz_composta = np.dot(matriz_translacao, np.dot(matriz_rotacao, matriz_translacao_inversa))

        return np.dot(matriz_composta, ponto)

    def cisalhamento(self, ponto, cx, cy):
        matriz_cisalhamento = np.array([[1, cx, 0],
                                        [cy, 1, 0],
                                        [0, 0, 1]], dtype=object)

        return np.dot(matriz_cisalhamento, ponto)

    def reflexaoEixo(self, ponto, eixo='x'):
        if eixo == 'x':
            matriz_reflexao = np.array([[1, 0, 0],
                                        [0, -1, 0],
                                        [0, 0, 1]], dtype=object)
        ## Y
        else:
            matriz_reflexao = np.array([[-1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, 1]], dtype=object)

        return np.dot(matriz_reflexao, ponto)

    def reflexaoLinha(self, ponto, linha='x'):
        if linha == 'x':
            matriz_reflexao = np.array([[0, 1, 0],
                                        [1, 0, 0],
                                        [0, 0, 1]], dtype=object)
        ## -X
        else:
            matriz_reflexao = np.array([[0, -1, 0],
                                        [-1, 0, 0],
                                        [0, 0, 1]], dtype=object)

        return np.dot(matriz_reflexao, ponto)
