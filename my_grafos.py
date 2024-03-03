# Connected Components
# Graph Algorithms 2023.2 - Federal University of Ceará
'''
Escreva um programa que receba um grafo não-direcionado e que escreva as suas componentes conexas. 
Uma componente conexa é um conjunto maximal de vértices ligados por caminhos no grafo. 

Write a program that takes an undirected graph and writes its connected components.
A connected component is a maximal set of vertices connected by paths in the graph.
'''

import sys

class Graph:
    # Initializing the graph
    # Define V (número de vértices do grafo) e o próprio grafo (lista de adjacência)
    # As it is a __init__ struct, it has no return
    def __init__(self, file):  
        for i, linha in enumerate(file):
            if i == 2:
                # pegar linha de index 2 e dar split no '='
                lista_aux = linha.split("=") # list with two elements
                n = int(lista_aux[1] ) #type cast pois está em forma de texto 
                # ex: ['n', '10']
                self.V = n # parametro orientado a objeto 

        G = [] # undirected graph
        # initializes an empty graph
        for i in range(0, n):
            edge = [] # aresta
            G.append(edge)
        self.G = G
        # self.grafo é lista de listas (uma lista para cada vértice)  

    def num_vertices(self):
        return self.V # method to return the number of vertices

    # Returns the filled graph
    def filling_graph(self, arquivo): # preencher o grafo de acordo com o input dos vértices
        for i, linha in enumerate(arquivo):
            if i >= 4: # começa na 5º linha
                linha_aux = linha.split() # split no espaço
                começo = int(linha_aux[0])
                fim = int(linha_aux[1])

                self.G[começo-1].append(fim-1)
                self.G[fim-1].append(começo-1)

        return self.G

    # BUSCA PROFUNDIDADE (DFS)

    # PRINTS CONNECTED COMPONENTS
    # Method with no return
    def connected_components(self):
        visited = [False] * len(self.G) # initializes all as unvisited
        component = [] # preencher componente e esvaziar a lista depois para o próximo componente
    
        # para cada vértice o (tratado como origem no loop) no grafo de V vértices
        for o in range(len(self.G)):
            if not visited[o]:
                component.append(o)
                visited[o] = True
                # visitar os vizinhos do vértice fixado como origem 'o'
                for v in component:
                    # se esse vértice visitado for vizinho e ainda não tiver sido visitado, 
                    for u in self.G[v]:
                    # add na componente conexa e o coloca como visitado (True)
                    # u será vizinho
                        if not visited[u]:
                            component.append(u)
                            visited[u] = True
                
                # Output
                component.sort() # Sorts the list in ascending order
                for j in range(len(component)): 
                    component[j] += 1 # para ficar a partir de 1 e não a partir de 0 o índice
                print(*component) # imprime separadamente a lista, linha por linha, sem []
                component.clear() # limpar para a próxima componente


# MAIN (test)

file = sys.stdin.readlines()
# read the lines of the file

''' Para testar com no VS Code 
- Arquivo teste.txt com um input teste

with open('comp_conexas_test.txt') as f:
    file = f.readlines() 
'''

my_graph = Graph(file) # create/ initialize the graph
# print(my_graph.num_vertices()) - num_vertices CORRECT 
# number of vertices
my_graph.filling_graph(file) # fills in the graph
my_graph.connected_components() # prints the connected components