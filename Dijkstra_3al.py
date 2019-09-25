
# Dijkstra - Shortest Path in Graph
from MinHeap import MinHeap
from FiboHeap import Fheap, Node
import time

class Vertex:
        
        def __init__(self, node):
                self.index = node
                self.adjacent = {}
                
        def add_neighbor(self, nei, weight):
                self.adjacent[nei] = weight
        
        def list_neighbors(self):
                return list(self.adjacent.keys())
        
        def get_weight(self, nei):
                if nei not in self.list_neighbors():
                        print('Connection is not exist.')
                        return
                return self.adjacent[nei]
        def __lt__(self, other_vertex):
                # vertex with index is number or digit
                return self.index < other_vertex.index


class Graph :
        
        def __init__(self, ver_dict = None):
                if ver_dict == None :
                        self.vertex_dict = {}
                else:
                        self.vertex_dict = ver_dict
                self.vertexes = []
                self.edges = []
                self.weights = []
        
        def number_vertexes(self):
                return len(self.vertexes)
        def number_edges(self):
                return len(self.edges)
                        
        def add_vertex(self, node):
                vertex = Vertex(node)
                if node in self.vertex_dict :
                        print('Vertex ' + node + ' was in graph.')
                else :
                        self.vertex_dict[node] = vertex
                        self.vertexes.append(node)
                                
        def add_connection(self, start_node, end_node, weight):
                if start_node not in self.vertex_dict :
                        self.add_vertex(start_node)
                if end_node not in self.vertex_dict :
                        self.add_vertex(end_node)
                self.vertex_dict[start_node].add_neighbor(self.vertex_dict[end_node], weight)
                self.edges.append((start_node, end_node))
                self.weights.append(weight)
        
        def add_edge(self, start_node, end_node, weight):
                self.add_connection(start_node, end_node, weight)
                self.vertex_dict[end_node].add_neighbor(self.vertex_dict[start_node], weight)
                self.edges.append((end_node, start_node))
                self.weights.append(weight)
                
        def get_vertex(self, node):
                if node not in self.vertex_dict:
                        print('Vertex ' + node + ' is not in graph.')
                        return
                return self.vertex_dict[node]
        
        def list_vertexes(self):
                return self.vertexes
                        
        def __iter__(self):
                return iter(self.vertex_dict.values())
        
        def __str__(self):
                print('Vertexes - Neighbors( Weight )')
                for v in self.list_vertexes() :
                        str2 = ''
                        vertex = self.vertex_dict[v]
                        for nei in vertex.list_neighbors():
                                str2 += ('  ' + str(nei.index) + '(' + str(vertex.get_weight(nei)) +')')
                        str1 = str(v) + ' '*(9 - len(str(v))) + '-'
                        print(str1 + str2)
                        
def extractMin_list(distance_ver, visited):
        list_ver = distance_ver.keys()
        min_val = float("INF")
        for v in list_ver:
                if distance_ver[v] < min_val and v not in visited:
                        min_val = distance_ver[v]
                        current_vertex = v
        return (min_val, current_vertex)

def Dijkstra_normal(G, start_node, end_node = None):
        n = G.number_vertexes()
        max_int = n*n
        distance_ver = {}
        path_ver = {}
        visited = []
        for vertex in G.__iter__():
                distance_ver[vertex.index] = max_int
        distance_ver[start_node] = 0
        while len(visited) != n :
                current_distance, current_vertex = extractMin_list(distance_ver, visited)
                visited.append(current_vertex)
                current_vertex = G.get_vertex(current_vertex)
                for nei in current_vertex.list_neighbors():
                        if nei.index in visited :
                                continue
                        distance = current_distance + current_vertex.get_weight(nei)
                        if distance < distance_ver[nei.index]:
                                distance_ver[nei.index] = distance
                                path_ver[nei.index] = current_vertex.index
        return [G, start_node, end_node, distance_ver, path_ver]      


def Dijkstra_MinHeap(G, start_node, end_node = None):
        n = G.number_vertexes()
        max_int = n*n
        distance_ver = {}
        path_ver = {}
        visited = []
        heap = MinHeap()
        for vertex in G.__iter__():
                distance_ver[vertex.index] = max_int
                heap.insertKey( (max_int, vertex.index) )
        distance_ver[start_node] = 0
        heap.insertKey((0, start_node))
        while len(visited)!=n:
                # O(Vlog(V)) complexity to loop and find min value vertex
                current_distance, current_vertex = heap.extractMin()
                if current_distance != distance_ver[current_vertex]:
                        continue
                visited.append(current_vertex)
                current_vertex = G.get_vertex(current_vertex)
                # O(Elog(V)) complexity to loop and decrease node
                for nei in current_vertex.list_neighbors():
                        if nei.index in visited :
                                continue
                        distance = current_distance + current_vertex.get_weight(nei)
                        if distance < distance_ver[nei.index]:
                                distance_ver[nei.index] = distance
                                heap.insertKey((distance, nei.index))   # O(log(V+)) = O(log(V))
                                path_ver[nei.index] = current_vertex.index
        return [G, start_node, end_node, distance_ver, path_ver]

def Dijkstra_FibHeap(G, start_node, end_node = None):
        n = G.number_vertexes()
        max_int = n*n
        distance_ver = {}
        path_ver = {}
        visited = []
        fheap = Fheap()
        for vertex in G.__iter__():
                distance_ver[vertex.index] = max_int
                fheap.insert(Node((max_int, vertex.index)))
        distance_ver[start_node] = 0
        fheap.insert(Node((0, start_node)))
        while len(visited) != n :
                # O(Vlog(V)) complexity to loop and find min value vertex
                node = fheap.extract_min()
                current_distance, current_vertex = node.key
                if current_distance != distance_ver[current_vertex]:
                        continue
                visited.append(current_vertex)
                current_vertex = G.get_vertex(current_vertex)
                # O(Elog(V)) complexity to loop and decrease node
                for nei in current_vertex.list_neighbors():
                        if nei.index in visited :
                                continue
                        distance = current_distance + current_vertex.get_weight(nei)
                        if distance < distance_ver[nei.index]:
                                distance_ver[nei.index] = distance
                                fheap.insert(Node((distance, nei.index)))   # O(log(V+)) = O(log(V))
                                path_ver[nei.index] = current_vertex.index
        return [G, start_node, end_node, distance_ver, path_ver]

def Dijkstra_path(return_fr_Dijkstra):
        [G, start_node, end_node, distance_ver, path_ver] = return_fr_Dijkstra
        if end_node == None:
                return { key.index : distance_ver[key] for key in distance_ver }, path_ver
        else:
                path = [end_node]
                curr_node = end_node
                while curr_node != start_node :
                        try :
                                curr_node = path_ver[curr_node]
                        except:
                                print("Not exist path to destination!")
                                return 100000, path[::-1]
                        path.append(curr_node)
                return distance_ver[G.get_vertex(end_node)], path[::-1]

        # Test Graph
#G = Graph()
#G.add_vertex('A')
#G.add_vertex('B')
#G.add_vertex('C')
#G.add_vertex('D')
#G.add_vertex('E')
#G.add_vertex('F')
#G.add_vertex('G')
#G.add_vertex('H')
#
#G.add_edge('A', 'B', 4)
#G.add_edge('A', 'C', 3)
#G.add_edge('B', 'C', 1)
#G.add_edge('B', 'D', 5)
#G.add_edge('C', 'E', 7)
#G.add_edge('D', 'E', 7)
#G.add_edge('D', 'F', 5)
#G.add_edge('D', 'G', 2)
#G.add_edge('E', 'G', 5)
#G.add_edge('F', 'G', 1)
#G.add_edge('F', 'H', 7)
#G.add_edge('G', 'H', 4)

#G.__str__()
#print(G.list_vertexes())
#G.edges
#G.number_vertexes()

# Test algorithm
#return_from_Dijkstra_1 = Dijkstra_normal(G, 'A')
#return_from_Dijkstra_2 = Dijkstra_MinHeap(G, 'A')
#return_from_Dijkstra_3 = Dijkstra_FibHeap(G, 'A')
#
#return_from_Dijkstra_1_path = Dijkstra_normal(G, 'A', 'F')
#l_path, path = Dijkstra_path(return_from_Dijkstra_1_path)


#import random
#import math
#import string
#def gen_random_fullGraph(num_ver):
#        Gr = Graph()
#        len_s_max = int(math.log(num_ver, 26)) + 1
#        l = []
#        while(True):
#                s = ''
#                for i in range(len_s_max):
#                        s1 = random.choice(string.ascii_uppercase)
#                        s += s1
#                if(s in l):
#                        continue
#                l.append(s)
#                Gr.add_vertex(s)
#                if len(l) == num_ver :
#                        break
#        for start in Gr.list_vertexes():
#                for end in Gr.list_vertexes():
#                        if end == start:
#                                continue
#                        weights = random.randint(1, num_ver)
#                        Gr.add_connection(start, end, weights)
#        return Gr
#G = gen_random_fullGraph(100)
#v = random.choice(G.list_vertexes())
#x = Dijkstra_MinHeap(G, v)
#y = Dijkstra_normal(G, v)
#z = Dijkstra_FibHeap(G, v)
#
#
#
#start_node = v
#n = G.number_vertexes()
#max_int = n*n
#distance_ver = {}
#path_ver = {}
#visited = []
#list_neiadded = []
#list_neichecked = []
#heap = MinHeap()
#for vertex in G.__iter__():
#        distance_ver[vertex.index] = max_int
#        heap.insertKey( (max_int, vertex.index) )
#distance_ver[start_node] = 0
#heap.insertKey((0, start_node))
#while len(visited)!=n:
#        # O(Vlog(V)) complexity to loop and find min value vertex
#        current_distance, current_vertex = heap.extractMin()
#        if current_distance != distance_ver[current_vertex]:
#                continue
#        visited.append(current_vertex)
#        current_vertex = G.get_vertex(current_vertex)
#        # O(Elog(V)) complexity to loop and decrease node
#        i = 0
#        j = 0
#        for nei in current_vertex.list_neighbors():
#                j += 1
#                if nei.index in visited :
#                        continue
#                distance = current_distance + current_vertex.get_weight(nei)
#                if distance < distance_ver[nei.index]:
#                        i += 1
#                        distance_ver[nei.index] = distance
#                        heap.insertKey((distance, nei.index))   # O(log(V+)) = O(log(V))
#                        path_ver[nei.index] = current_vertex.index
#        list_neiadded.append(i)
#        list_neichecked.append(j)
#        # Test GraphDrawing.py
#from GraphDrawing import Graph_Drawing
#import matplotlib.pyplot as plt
#Drawing = Graph_Drawing(G)
#plt.figure(1)
#position = Drawing.draw_graph()
#plt.figure(2)
#Drawing.draw_path(path, position)
