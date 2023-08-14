from funcs import cria_grafo, cria_grafo_completo, \
                  cria_grafo_bipartido_completo, cria_grafo_estrela, \
                  cria_grafo_caminho, cria_grafo_ciclo, \
                  cria_grafo_roda, cria_grafo_cubo 
from conexa import grafo_conexo

data_set = {}

while True:
    
    menu_escolha = input("O que deseja fazer? \
                          \na - Criar um grafo \
                          \nb - Informações sobre um grafo criado \
                          \nc- Criar grafo especial \
                          \nd- Verificar se um grafo é conexo \
                          \ne- Sair\n")

    if menu_escolha == "a": 
        nome_grafo = input("Qual será o nome do grafo? ")
        mat_adj_grafo, qtd_arestas = cria_grafo()
        data_set[nome_grafo] = (mat_adj_grafo, qtd_arestas)
    
    elif menu_escolha == "b":
        grafo_buscado = input("Digite o nome do grafo buscado:\n:")

        if grafo_buscado in data_set:
            print("Matriz de adjacencia do grafo: ")

            for item in data_set[grafo_buscado][0]:
                print(item)

            print("Quantidade de arestas no grafo")
            print(data_set[grafo_buscado][1])

        else:
            print("O grafo não existe no sistema \
                  ,verifique que o nome está correto, ou crie um!")
    elif menu_escolha == "c":
        grafo_especial = input("Qual tipo de grafo você deseja construir? \
                               \na-Completo \
                               \nb-Bipartido Completo \
                               \nc-Estrela \
                               \nd-Caminho \
                               \ne-Ciclo \
                               \nf-Roda \
                               \ng-Cubo\n:")

        if grafo_especial == "a":

            nome_grafo = input("Qual será o nome do grafo? ")
            mat_adj_grafo_completo, qtd_arestas = cria_grafo_completo()
            data_set[nome_grafo] = (mat_adj_grafo_completo, qtd_arestas)
        
        elif grafo_especial == "b":

            nome_grafo = input("Qual será o nome do grafo? ")
            mat_adj_grafo_bipartido_completo, qtd_arestas = cria_grafo_bipartido_completo()
            data_set[nome_grafo] = (mat_adj_grafo_bipartido_completo, qtd_arestas)
        
        elif grafo_especial == "c":

            nome_grafo = input("Qual será o nome do grafo? ")
            mat_adj_grafo_estrela, qtd_arestas = cria_grafo_estrela()
            data_set[nome_grafo] = (mat_adj_grafo_estrela, qtd_arestas)
        
        elif grafo_especial == "d":

            nome_grafo = input("Qual será o nome do grafo? ")
            mat_adj_grafo_caminho, qtd_arestas = cria_grafo_caminho()
            data_set[nome_grafo] = (mat_adj_grafo_caminho, qtd_arestas)
        
        elif grafo_especial == "e":

            nome_grafo = input("Qual será o nome do grafo? ")
            mat_adj_grafo_ciclo, qtd_arestas = cria_grafo_ciclo()
            data_set[nome_grafo] = (mat_adj_grafo_ciclo, qtd_arestas)

        elif grafo_especial == "f":

            nome_grafo = input("Qual será o nome do grafo? ")
            mat_adj_grafo_roda, qtd_arestas = cria_grafo_roda()
            data_set[nome_grafo] = (mat_adj_grafo_roda, qtd_arestas)

        elif grafo_especial == "g":

            nome_grafo = input("Qual será o nome do grafo? ")
            mat_adj_grafo_cubo, qtd_arestas = cria_grafo_cubo()
            data_set[nome_grafo] = (mat_adj_grafo_cubo, qtd_arestas)

    elif menu_escolha == "d":
        grafo_buscado = input("Digite o nome do grafo buscado:\n:")
        
        if grafo_buscado in data_set:
            print("Matriz de adjacencia do grafo: ")

            for item in data_set[grafo_buscado][0]:
                print(item)

            """
            print("Quantidade de arestas no grafo")
            print(data_set[grafo_buscado][1])
            """
            conexo, ccs = grafo_conexo(data_set[grafo_buscado][0])
            if conexo:
                print('Grafo conexo', ccs)
            else:
                print('Grafo desconexo\nNúmero de componentes conexas: ', ccs)
    
        else:
            print("O grafo não existe no sistema, verifique que o nome está correto, ou crie um!")
    elif menu_escolha == "e":
       break
    else:
        print("Selecione uma escolha válida")
