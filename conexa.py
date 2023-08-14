# Calculamos quantas componentes conexas um grafo possui
# baseados na sua matriz de adjacência
from collections import deque
global mat_vertices_obj
mat_vertices_obj = []


class Vertice():
    def __init__(self, p, cor, d, vertice):
        self.p = p
        self.cor = cor
        self.d = d
        self.vertice = vertice  # Indica qual o número do vértice. 
        # Serve para nos encontrarmos na matriz de adjacência
        self.vizinhos = []  # A quem ele está conectado
        # self.status = status # Ativo(aresta) ou não


def buscando(inicio):
    Q = deque()
    s = mat_vertices_obj[inicio]
    s.cor = "Cinza"
    s.d = 0
    Q.append(s)

    while len(Q) != 0:
        u = Q.pop()

        for item in u.vizinhos:
            if mat_vertices_obj[item].cor == "Branco":
                mat_vertices_obj[item].cor = "Cinza"
                mat_vertices_obj[item].d += 1
                mat_vertices_obj[item].p = u
                Q.append(mat_vertices_obj[item])
        u.cor = "Preto"


def grafo_conexo(mat):
    global mat_vertices_obj

    # Vamos preencher tudo de branco
    # andamos apenas pela diagonal principal para salvar tempo e memória
    # mat_vertices_obj = []
    for v, i in enumerate(mat):
        vertice = Vertice(None, "Branco", 9999, v)
        for item in range(0, len(mat)):
            # vertice = Vertice(None,"Branco", 9999, v)#, mat[v][item])
            if mat[v][item] == 1:
                # Vamos add item
                vertice.vizinhos.append(item)
        mat_vertices_obj.append(vertice)

    # Agora começa o algortimo mesmo
    cc = 0  # Numero de componentes conexas
    for i, item in enumerate(mat_vertices_obj):
        if item.cor == "Branco":
            buscando(i)
            cc += 1

    mat_vertices_obj = []
    if cc == 1:
        return True, cc
    else:
        return False, cc
