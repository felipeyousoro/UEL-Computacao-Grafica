import numpy as np
import transformada2d

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

    print("Pontos iniciais:")
    for ponto in pontos:
        print("(X,Y) = ({},{})".format(ponto[0][0], ponto[1][0]))

    ## Exemplo de uso
    print("Translação:")
    for ponto in pontos:
        ponto = transformada.translacao(ponto, 2, 2)
        print("(X,Y) = ({},{})".format(ponto[0][0], ponto[1][0]))

