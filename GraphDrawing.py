import numpy as np
import matplotlib.pyplot as plt
import pylab
import networkx as nx


class Graph_Drawing:
        def __init__(self, Graph):
                self.G = Graph
                self.Gx = nx.DiGraph()
                self.len = Graph.number_vertexes()
        def draw_graph(self, pos = None):
                for i in range(self.G.number_edges()):
                        self.Gx.add_edge(self.G.edges[i][0], self.G.edges[i][1], weight = self.G.weights[i])
                Gx = self.Gx
                if pos == None :
                        pos = nx.spring_layout(Gx, scale = 1.0)
                
                edge_labels=dict([((u,v),d['weight']) for u,v,d in Gx.edges(data=True)])
                edgewidth = [d['weight'] for (u,v,d) in Gx.edges(data=True)]
                node_labels = {node : node for node in Gx.nodes()}
                n = self.len
                a1 = int(400*10/n)
                a2 = int(8*10/n)
                a3 = [int(i*10/n) for i in edgewidth]
                a4 = int(12*10/n)
                
                nx.draw_networkx_nodes(Gx, pos, node_color = 'green', node_size = a1, font_size = 12)
                nx.draw_networkx_edge_labels(Gx, pos, font_size = a2, font_color = 'black', edge_labels=edge_labels)
                nx.draw_networkx_edges(Gx, pos, width = a3, edge_color = 'blue')
                nx.draw_networkx_labels(Gx, pos, font_size = a4, font_color = 'black', labels=node_labels)
#                nx.draw_networkx_nodes(Gx, pos, node_color = 'green', node_size = 400, font_size = 12)
#                nx.draw_networkx_edge_labels(Gx, pos, font_size = 8, font_color = 'black', edge_labels=edge_labels)
#                nx.draw_networkx_edges(Gx, pos, width = edgewidth, edge_color = 'blue')
#                nx.draw_networkx_labels(Gx, pos, font_size = 12, font_color = 'black', labels=node_labels)
                #nx.draw(Gx,pos, **options, edge_cmap=plt.cm.Reds)
                plt.plot()
                return pos

        def draw_path(self, path, pos = None):
                for i in range(self.G.number_edges()):
                        self.Gx.add_edge(self.G.edges[i][0], self.G.edges[i][1], weight = self.G.weights[i])
                Gx = self.Gx
                if pos == None :
                        pos = nx.spring_layout(Gx)
                
                edge_labels=dict([((u,v),d['weight']) for u,v,d in Gx.edges(data=True)])
                edgewidth = [d['weight'] for (u,v,d) in Gx.edges(data=True)]
                red_edges = []
                for i in range(len(path) - 1):
                        red_edges.append((path[i], path[i+1]))
                edge_colors = ['blue' if not edge in red_edges else 'red' for edge in self.Gx.edges()]
                edgewidth = [d['weight']*2 for (u,v,d) in self.Gx.edges(data=True)]

                nx.draw_networkx_nodes(Gx, pos, node_color = 'green', node_size = 400, font_size = 12)
                node_labels = {node : node for node in Gx.nodes()}
                nx.draw_networkx_edge_labels(Gx, pos, font_size = 8, font_color = 'black', edge_labels=edge_labels)
                nx.draw_networkx_edges(self.Gx, pos, width=edgewidth, edge_color = edge_colors)
                nx.draw_networkx_labels(Gx, pos, font_color = 'black', labels=node_labels)
#                nx.draw(Gx,pos, **options, arrowsize=20, arrowstyle='fancy')

                return pos