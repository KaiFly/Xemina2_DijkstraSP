
# Dijkstra - Shortest Path in Graph
from MinHeap import MinHeap
from FiboHeap import makefheap, fheappush, fheappop
import heapq
import fibheap
from GraphDrawing import Graph_Drawing


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


def Dijkstra_normal_original(G, start_node, end_node = None):

        distance_ver = {}
        visited_ver = []
        path_ver = {}
        # O(V) complexity to add vertexes to dict
        for vertex in G.__iter__():
                distance_ver[vertex] = float("INF")
        distance_ver[G.get_vertex(start_node)] = 0
        # O(V) complexity to loops through all vertexes
        while len(visited_ver) < G.number_vertexes():
                # O(V) complexity to find current vertex
                min_value = float("INF")
                for v in distance_ver :
                        if v in visited_ver :
                                continue
                        if distance_ver[v] < min_value:
                                min_value = distance_ver[v]
                                min_ver = v
                current_vertex = min_ver
                visited_ver.append(current_vertex)
                # O(V) complexity to check neighbors
                for nei in current_vertex.list_neighbors():
                        if nei in visited_ver :
                                continue
                        else :
                                dist = distance_ver[current_vertex] + current_vertex.get_weight(nei)
                                distance_ver[nei] = min(dist, distance_ver[nei])
                                path_ver[nei.index] = current_vertex.index
        if end_node == None:
                return { key.index : distance_ver[key] for key in distance_ver }, path_ver
        else:
                path = [end_node]
                curr_node = end_node
                while curr_node != start_node :
                        curr_node = path_ver[curr_node]
                        path.append(curr_node)
                return distance_ver[G.get_vertex(end_node)], path[::-1]
        

def Dijkstra_normal(G, start_node, end_node = None):
        distance_ver = {}
        path_ver = {}
        for vertex in G.__iter__():
                distance_ver[vertex] = float("INF")
        distance_ver[G.get_vertex(start_node)] = 0
        normal_queue = [(0, G.get_vertex(start_node))]
        while normal_queue:
                # O(Vlog(V)) complexity to loop and find min value vertex
                min_val = float("INF")
                for elem in normal_queue:
                        if elem[0] < min_val :
                                min_val = elem[0]
                                current_vertex = elem[1]
                current_distance = min_val
                normal_queue.remove((current_distance, current_vertex))
                if current_distance > distance_ver[current_vertex]:
                        continue
                # O(Elog(V)) complexity to loop and push node
                for nei in current_vertex.list_neighbors():
                        distance = current_distance + current_vertex.get_weight(nei)
                        if distance < distance_ver[nei]:
                                distance_ver[nei] = distance
                                normal_queue.append((distance, nei))   # O(log(V))
                                path_ver[nei.index] = current_vertex.index
        return [G, start_node, end_node, distance_ver, path_ver]


def Dijkstra_MinHeap(G, start_node, end_node = None):
        distance_ver = {}
        path_ver = {}
        for vertex in G.__iter__():
                distance_ver[vertex] = float("INF")
        distance_ver[G.get_vertex(start_node)] = 0
        heap = [(0, G.get_vertex(start_node))]
        while heap:
                # O(Vlog(V)) complexity to loop and find min value vertex
                current_distance, current_vertex = heapq.heappop(heap)
                if current_distance > distance_ver[current_vertex] :
                        continue
                # O(Elog(V)) complexity to loop and push node
                for nei in current_vertex.list_neighbors():
                        distance = current_distance + current_vertex.get_weight(nei)
                        if distance < distance_ver[nei]:
                                distance_ver[nei] = distance
                                heapq.heappush(heap, (distance, nei))   # O(log(V))
                                path_ver[nei.index] = current_vertex.index
        return [G, start_node, end_node, distance_ver, path_ver]


#from fibheap import makefheap, fheappush, fheappop
def Dijkstra_FibHeap(G, start_node, end_node = None):
        distance_ver = {}
        path_ver = {}
        fheap = makefheap()
        for vertex in G.__iter__():
                if vertex == G.get_vertex(start_node):
                        continue
                distance_ver[vertex] = float("INF")
        distance_ver[G.get_vertex(start_node)] = 0
        fheappush(fheap, (0, G.get_vertex(start_node)))
        while fheap.num_nodes:
                # O(Vlog(V)) complexity to loop and find min value vertex
                current_distance, current_vertex = fheappop(fheap)
                if current_distance > distance_ver[current_vertex] :
                        continue
                # O(Elog(V)) complexity to loop and push node
                for nei in current_vertex.list_neighbors():
                        distance = current_distance + current_vertex.get_weight(nei)
                        if distance < distance_ver[nei]:
                                distance_ver[nei] = distance
                                fheappush(fheap, (distance, nei))   # O(log(V))
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
#G.add_connection('A', 'B', 4)
#G.add_connection('A', 'D', 1)
#G.add_connection('A', 'C', 7)
#G.add_connection('B', 'C', 2)
#G.add_connection('C', 'E', 2)
#G.add_connection('C', 'F', 3)
#G.add_connection('D', 'B', 2)
#G.add_connection('D', 'E', 4)
#G.add_connection('E', 'B', 0.01)
#G.add_connection('E', 'D', 3)
#G.add_connection('F', 'E', 1)
##G.__str__()
#print(G.list_vertexes())
#G.edges

        # Test algorithm
#return_from_Dijkstra_1 = Dijkstra_normal(G, 'A')
#return_from_Dijkstra_2 = Dijkstra_MinHeap(G, 'A')
#return_from_Dijkstra_3 = Dijkstra_FibHeap(G, 'A')
#
#return_from_Dijkstra_1_path = Dijkstra_normal(G, 'A', 'F')
#l_path, path = Dijkstra_path(return_from_Dijkstra_1_path)
#Dijkstra_FibHeap(G, 'A', 'F')

        # Test GraphDrawing.py
#import matplotlib.pyplot as plt
#Drawing = Graph_Drawing(G)
#plt.figure(1)
#position = Drawing.draw_graph()
#plt.figure(2)
#Drawing.draw_path(path, position)

