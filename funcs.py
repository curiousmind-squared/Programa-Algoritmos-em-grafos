def custom_input(lower_range: int, upper_range: int, mensagem: str = "",
                 mensagem_de_erro: str = "Favor, digite um número") -> int:
    gatekeeper = True
    while gatekeeper:
        try:
            num = int(input(mensagem))
            if num < lower_range or num > upper_range:
                raise ValueError
        except ValueError:
            print(mensagem_de_erro)
        else:
            gatekeeper = False
    return num


def cria_grafo():
    n = custom_input(0, 9999, 
                     "Digite n: ", 
                     "Escolha inválida, \
                     certifique-se de que selecionou um inteiro positivo")

    mat_adj = [[0 for j in range(0, n)] for i in range(0, n)]
    qtd_aresta = 0

    for i in range(0, n):
        for j in range(i, n):

            print("Existe uma aresta que conecta ", i, "a", j,
                  "?\n1 - Sim\n0 - Não\n", end='')
            aresta = custom_input(0,
                                  1,
                                  mensagem_de_erro="Escolha inválida, \
                                  certifique-se de que selecinou 0 ou 1")
            
            if aresta == 1:
                qtd_aresta += 1

            # é uma matriz simétrica
            mat_adj[i][j] = aresta
            mat_adj[j][i] = aresta
    
    return mat_adj, qtd_aresta


def cria_grafo_completo():
    n = custom_input(1, 9999, "Digite n: ", 
                     "Escolha inválida,\
                     certifique-se de que selecionou um inteiro positivo")
    mat_adj = [[0 for j in range(0, n)] for i in range(0, n)]

    for i in range(0, n):
        for j in range(i, n):            
            if i == j:
                mat_adj[i][j] = 0
            else:
                mat_adj[i][j] = 1
                mat_adj[j][i] = 1

    qtd_aresta = int((n*(n - 1)/2))
    return mat_adj, qtd_aresta 


def cria_grafo_bipartido_completo():
    n1 = custom_input(1, 9999, "Digite n1: ", 
                      "Escolha inválida, \
                       certifique-se de que selecionou um inteiro positivo")
    n2 = custom_input(1, 9999, "Digite n2: ", 
                      "Escolha inválida, \
                       certifique-se de que selecionou um inteiro positivo")

    tot = n1+n2
    adj_matrix = [[0 for j in range(0, tot)] for i in range(0, tot)]
    for i in range(n1):
        for j in range(n1, n1 + n2):
            adj_matrix[i][j] = 1
            adj_matrix[j][i] = 1

    qtd_arestas = n1*n2
    return adj_matrix, qtd_arestas 


def cria_grafo_estrela():
    n = custom_input(1, 9999, "Digite n: ", 
                     "Escolha inválida, \
                      certifique-se de que selecionou um inteiro positivo")
    mat_adj = [[0 for j in range(0, n+1)] for i in range(0, n+1)]

    for i in range(1, n+1):
        mat_adj[i][0] = 1
        mat_adj[0][i] = 1

    return mat_adj, n


def cria_grafo_caminho():
    n = custom_input(1, 9999, "Digite n: ", 
                     "Escolha inválida, \
                      certifique-se de que selecionou um inteiro positivo")

    mat_adj = [[0 for j in range(0, n)] for i in range(0, n)]

    # Primeira e ultima linha sempre serão iguais
    for i in range(0, n):
        # Primeira linha
        if i == 0:
            mat_adj[i][1] = 1
        # Ultima linha
        elif i == n-1:
            mat_adj[i][n-2] = 1
        # Todas as outras seguem esse padrão de um 0 na diagonal principal 
        # e 1 adjacente a esse 0
        else:
            mat_adj[i][i-1] = 1
            mat_adj[i][i] = 0
            mat_adj[i][i+1] = 1

    qtd_arestas = n-1
    return mat_adj, qtd_arestas 


def cria_grafo_ciclo():
    n = custom_input(3, 9999, "Digite n(deve ser maior do que 3): ", 
                     "Escolha inválida, \
                      certifique-se de que selecionou um inteiro \
                      maior ou igual a 3")

    mat_adj = [[0 for j in range(0, n)] for i in range(0, n)]

    for i in range(0, n):
        # Primeira linha, se conecta ao segundo e ao utimo
        if i == 0:
            mat_adj[i][1] = 1
            mat_adj[i][n-1] = 1

        # Ultima linha, se conecta ao penultimo e ao primeiro
        elif i == n-1:
            mat_adj[i][n-2] = 1
            mat_adj[i][0] = 1
        # O resto é igual a um caminho
        else:
            mat_adj[i][i-1] = 1
            mat_adj[i][i] = 0
            mat_adj[i][i+1] = 1
    
    return mat_adj, n


def cria_grafo_roda():
    n = custom_input(3, 9999, "Digite n(deve ser maior do que 3): ",
                     "Escolha inválida, \
                      certifique-se de que selecionou um inteiro \
                      maior ou igual a 3")
    mat_adj = [[0 for j in range(0, n)] for i in range(0, n)]

    # Nada mais do que uma mistura de um grafo Estrela com um Ciclo

    for i in range(0, n):
        # Estrela
        mat_adj[i][0] = 1
        mat_adj[0][i] = 1

        # Ciclo(Adaptado)
        if i == 1:  
            # Primeiro vértice de um grafo ciclo, 
            # se conecta ao segundo e ao ultimo
            mat_adj[i][2] = 1
            mat_adj[i][n-1] = 1
        elif i == n-1:  
            # Ultimo vértice de um grafo ciclo
            # se concecta ao penultimo e ao primeiro
            mat_adj[i][1] = 1
            mat_adj[i][n-2] = 1
        else:
            mat_adj[i][i-1] = 1
            mat_adj[i][i] = 0
            mat_adj[i][i+1] = 1

    mat_adj[0][0] = 0

    qtd_arestas = 2*(n-1)

    return mat_adj, qtd_arestas


def diagonal_secundaria(n, mat):
    for i in range(n):
        mat[i][n-i-1] = 1
    return mat


def grafo_cubo(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [[0, 1], [1, 0]]
    else:
        mat_adj_rec = [[0 for j in range(0, 2**(n-1))] 
                       for i in range(0, 2**(n-1))]
        mat_adj_easy = [[0 for j in range(0, 2**(n-1))] 
                        for i in range(0, 2**(n-1))]

        # Vamos preencher a parte da matriz com a diagonal secundaria 1 
        # e resto 0
        mat_adj_easy = diagonal_secundaria(2**(n-1), mat_adj_easy)

        # Vamos entrar na recursão!
        mat_adj_rec = grafo_cubo(n-1)

        cp_mat_adj_rec = mat_adj_rec.copy()

        for v, i in enumerate(mat_adj_rec):
            mat_adj_rec[v] = mat_adj_rec[v]+mat_adj_easy[v]
            mat_adj_easy[v] = mat_adj_easy[v]+cp_mat_adj_rec[v]

        mat_adj = mat_adj_rec + mat_adj_easy

        return mat_adj


def cria_grafo_cubo():
    n = custom_input(0, 9999, 
                     "Digite a classe do grafo n-cubo \
                      (0 para q0, 1 para q1 e etc): ", 
                     "Escolha inválida, \
                      certifique-se de que selecionou um inteiro não-negativo")
    mat = grafo_cubo(n)
    qtd_arestas = 2**(n-1)*n
    return mat, qtd_arestas 


def grafo_conexo(grafo):
    # Apenas testando a função
    return True, 2
