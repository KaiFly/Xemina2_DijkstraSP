# Dijkstra - Shortest Path in Graph

import networkx as nx
import matplotlib.pyplot as plt


class Graph :
        
        def __init__(self, graph_dict : dict):
                self.graph_dict = graph_dict
                
        def list_vertices(self):
                return list(self.graph_dict.keys())
        
        def list_edges(self):
                edges = []
                for v in self.graph_dict :
                        for nei in self.graph_dict[v]:
                                if (nei, v) not in edges :
                                        edges.append((v, nei))
                return edges
        
        def add_vertice(self, vertice : int):
                if vertice in self.graph_dict :
                        print('Vertice was in graph.')
                else :
                        self.graph_dict[vertice] = []
        
        def add_edge(self, edge : tuple):
                v, nei = edge[0], edge[1]
                if v not in self.graph_dict :
                        self.graph_dict[v] = [nei]
                else :
                        if nei in self.graph_dict[v] :
                                print('Edge existed.')
                        else :
                                self.graph_dict[v].append(nei)
        
        def draw_graph(self):
                G = nx.Graph()
                G.add_edges_from(d.list_edges())
                options = {
                            'node_color': 'blue',
                            'node_size': 300,
                            'width': 3,
                            'edge_color': 'black',
                            'font_size': 12
                          }
                weights = {}
                for i in range(len(d.list_edges())):
                        weights[d.list_edges()[i]] = i + 1
                pos = nx.spring_layout(G)
                nx.draw_networkx(G, pos=pos, style = 'dashed', **options) #, style = 'dashed', **options
                nx.draw_networkx_edge_labels(G, pos=pos, edge_labels = weights)
                nx.draw_networkx_edges(G,pos,width=4, edge_color='g', arrows=False)

        def draw_shortestPath(self, start_vertice, end_vertice):
                # Need Dijkstra and parallel Dijkstra here
                return
                
        def __str__(self):
                print('Vertices - Neighbors')
                for v in self.list_vertices() :
                        str2 = ''
                        for nei in self.graph_dict[v]:
                                str2 += ('  ' + str(nei))
                        str1 = str(v) + ' '*(9 - len(str(v))) + '-'
                        print(str1 + str2)


d = Graph({1: [2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 3], 3 : [1, 2, 4], 4 : [1, 3, 5], 5: [1, 4]})
print(d.list_vertices())
print(d.list_edges())
print(d.__str__())
d.draw_graph()
                        


