import matplotlib.pyplot as plt
#matplotlib.use('GTKAgg')

import networkx as nx
import math
from FiboHeap import makefheap, fheappush, fheappop 
from test_complexity import gen_random_fullGraph, gen_random_graph
import time
from heapq import heappush, heappop
import random

def animated_Dijkstra_normal(G, Gx, pos, start_node, n):
#        if n >= 300:
        time_excess = 0
        distance_ver = {}
        for vertex in G.__iter__():
                distance_ver[vertex] = float("INF")
        distance_ver[G.get_vertex(start_node)] = 0
        normal_queue = [(0, G.get_vertex(start_node))]
        while normal_queue:
                min_val = float("INF")
                for elem in normal_queue:
                        if elem[0] < min_val :
                                min_val = elem[0]
                                current_vertex = elem[1]
                current_distance = min_val
                normal_queue.remove((current_distance, current_vertex))
                if current_distance > distance_ver[current_vertex]:
                        continue
                nx.draw_networkx_nodes(G, pos, nodelist = [current_vertex.index], node_color = 'red', node_size = 200, font_size = 12)
                for nei in current_vertex.list_neighbors():
                        distance = current_distance + current_vertex.get_weight(nei)
                        if distance < distance_ver[nei]:
                                t1 = time.time()
                                plt.pause(1e-32) 
                                time_excess += (time.time()-t1)
                                distance_ver[nei] = distance
                                normal_queue.append((distance, nei))
                                nx.draw_networkx_edges(Gx, pos, edgelist = [(current_vertex.index, nei.index)],  width = 1.5, edge_color = 'red')
        return time_excess

def animated_Dijkstra_MinHeap(G, Gx, pos, start_node, n):
        time_excess = 0
        distance_ver = {}
        for vertex in G.__iter__():
                if vertex == G.get_vertex(start_node):
                        continue
                distance_ver[vertex] = float("INF")
        distance_ver[G.get_vertex(start_node)] = 0
        heap = [(0, G.get_vertex(start_node))]
        while heap:
                current_distance, current_vertex = heappop(heap)
                if current_distance > distance_ver[current_vertex] :
                        continue
                nx.draw_networkx_nodes(G, pos, nodelist = [current_vertex.index], node_color = 'red', node_size = 200, font_size = 12)
           
                for nei in current_vertex.list_neighbors():
                        distance = current_distance + current_vertex.get_weight(nei)
                        if distance < distance_ver[nei]:
                                t1 = time.time()
                                plt.pause(1e-32)
                                time_excess += (time.time() - t1)
                                distance_ver[nei] = distance
                                heappush(heap, (distance, nei))
                                nx.draw_networkx_edges(Gx, pos, edgelist = [(current_vertex.index, nei.index)],  width = 1.5, edge_color = 'red')
        return time_excess

def animated_Dijkstra_MinHeap_path(G, Gx, pos, start_node, end_node, n):
        time_excess = 0
        path_ver = {}
        distance_ver = {}
        heap = makefheap()
        for vertex in G.__iter__():
                if vertex == G.get_vertex(start_node):
                        continue
                distance_ver[vertex] = float("INF")
        distance_ver[G.get_vertex(start_node)] = 0
        heap = [(0, G.get_vertex(start_node))]
        while heap:
                current_distance, current_vertex = heappop(heap)
                if current_distance > distance_ver[current_vertex] :
                        continue
                nx.draw_networkx_nodes(G, pos, nodelist = [current_vertex.index], node_color = 'red', node_size = 200, font_size = 12)
                if current_vertex.index == end_node:
                        path = [end_node]
                        curr_node = end_node
                        while curr_node != start_node :
                                try :
                                        curr_node = path_ver[curr_node]
                                except:
                                        plt.text(-1.01,0, 'Dont exist way.')
                                path.append(curr_node)
                        path = path[::-1]
                        for i in range(len(path)-1):
                                nx.draw_networkx_edges(Gx, pos, edgelist = [(path[i], path[i+1])],  width = 3, edge_color = 'black')
                        plt.text(-1.05,-1.05,'Path ({}):'.format(distance_ver[current_vertex]) + str(path[::-1]), fontsize = 8)
                        return time_excess                        
                for nei in current_vertex.list_neighbors():
                        distance = current_distance + current_vertex.get_weight(nei)
                        if distance < distance_ver[nei]:
                                t1 = time.time()
                                plt.pause(1e-32)
                                time_excess += (time.time() - t1)
                                distance_ver[nei] = distance
                                heappush(heap, (distance, nei))   # O(log(V))
                                nx.draw_networkx_edges(Gx, pos, edgelist = [(current_vertex.index, nei.index)],  width = 1.5, edge_color = 'red')
                                path_ver[nei.index] = current_vertex.index
        return time_excess

def animated_Dijkstra_FibHeap(G, Gx, pos, start_node, n):
        time_excess = 0
        distance_ver = {}
        fheap = makefheap()
        for vertex in G.__iter__():
                if vertex == G.get_vertex(start_node):
                        continue
                distance_ver[vertex] = float("INF")
        distance_ver[G.get_vertex(start_node)] = 0
        fheappush(fheap, (0, G.get_vertex(start_node)))
        while fheap:
                current_distance, current_vertex = fheappop(fheap)
                if current_distance > distance_ver[current_vertex] :
                        continue
                nx.draw_networkx_nodes(G, pos, nodelist = [current_vertex.index], node_color = 'red', node_size = 200, font_size = 12)
           
                for nei in current_vertex.list_neighbors():
                        distance = current_distance + current_vertex.get_weight(nei)
                        if distance < distance_ver[nei]:
                                t1 = time.time()
                                plt.pause(1e-32)
                                time_excess += (time.time - t1)
                                distance_ver[nei] = distance
                                fheappush(fheap, (distance, nei))
                                nx.draw_networkx_edges(Gx, pos, edgelist = [(current_vertex.index, nei.index)],  width = 1.5, edge_color = 'red')
        return time_excess


def initialize_fullGr(G, Gx, pos, start_node, n):
        plt.figure()
        node_labels = {node : node for node in Gx.nodes()}
        edge_labels=dict([((u,v),d['weight']) for u,v,d in Gx.edges(data=True)])
        font_label_size = 4
#        font_label_size = 8/(math.sqrt(n)*4)
        nx.draw_networkx_nodes(Gx, pos, node_color = 'green', node_size = 200, font_size = 12)
        nx.draw_networkx_edges(Gx, pos, width = 0.5, edge_color = 'blue')
        nx.draw_networkx_edge_labels(Gx, pos, label_pos = 0.2, font_size = font_label_size, font_color = 'black', edge_labels=edge_labels)
        nx.draw_networkx_labels(Gx, pos, font_size = 5, font_color = 'black', labels=node_labels)
        plt.plot()
        nx.draw_networkx_nodes(G, pos, nodelist = [start_node], node_color = 'yellow', node_size = 320, font_size = 12)
        plt.pause(5)

def plot_DMinHeap(G, Gx, pos, start_node, n):
        # Min Heap
        initialize_fullGr(G, Gx, pos, start_node, n)
        plt.title('Dijkstra MinHeap \nGraph |V| = ('+str(n)+') '+'\nSource : ' + start_node  , loc = 'left')
        start_time = time.time()
        time_excess = animated_Dijkstra_MinHeap(G, Gx, pos, start_node, n)
        end_time = time.time()
        print(time_excess)
        plt.title('Done\n Run time : ' + "%.5f" % (end_time - start_time - time_excess) + '(s)', color ='red', loc = 'right')

def plot_DFibHeap(G, Gx, pos, start_node, n):
        # Fibonacci Heap
        initialize_fullGr(G, Gx, pos, start_node, n)
        plt.title('Dijkstra MinHeap \nGraph |V| = ('+str(n)+') '+'\nSource : ' + start_node  , loc = 'left')
        start_time = time.time()
        time_excess = animated_Dijkstra_normal(G, Gx, pos, start_node, n)
        print(time_excess)
        end_time = time.time()
        plt.title('Done\n Run time : ' + "%.5f" % (end_time - start_time - time_excess) + '(s)', color ='red', loc = 'right')
        
def plot_Normal(G, Gx, pos, start_node, n):
        initialize_fullGr(G, Gx, pos, start_node, n)
        plt.title('Dijkstra MinHeap \nGraph |V| = ('+str(n)+') '+'\nSource : ' + start_node  , loc = 'left')
        start_time = time.time()
        time_excess = animated_Dijkstra_normal(G, Gx, pos, start_node, n)
        print(time_excess)
        end_time = time.time()
        plt.title('Done\n Run time : ' + "%.5f" % (end_time - start_time - time_excess) + '(s)', color ='red', loc = 'right')
        
def plot_DMinHeap_path(G, Gx, pos, start_node, end_node, n):
        initialize_fullGr(G, Gx, pos, start_node, n)
        nx.draw_networkx_nodes(G, pos, nodelist = [end_node], node_color = 'yellow', node_size = 320, font_size = 12)
        plt.title('Dijkstra MinHeap \nGraph |V| = ('+str(n)+') '+'\nSource - Destination: ' + start_node + ' - ' + end_node , loc = 'left')
        start_time = time.time()
        time_excess = animated_Dijkstra_MinHeap_path(G, Gx, pos, start_node, end_node, n)
        end_time = time.time()
        print(time_excess)
        plt.title('Done\n Run time : ' + "%.5f" % (end_time - start_time - time_excess) + '(s)', color ='red', loc = 'right')

#n = 50
#G = gen_random_fullGraph(n)

n = 10
G = gen_random_graph(n, 30)
start_node = random.choice(G.list_vertexes())
end_node = random.choice(G.list_vertexes())
end_node == start_node

Gx = nx.DiGraph()
for i in range(G.number_edges()):
        Gx.add_edge(G.edges[i][0], G.edges[i][1], weight = G.weights[i])
pos = nx.spring_layout(Gx, k = 0.3*1/math.sqrt(n), iterations = 1, scale = 1.0)
#initialize_fullGr(G, Gx, pos, start_node, n)

plot_Normal(G, Gx, pos, start_node, n)
plot_DFibHeap(G, Gx, pos, start_node, n)
plot_DMinHeap(G, Gx, pos, start_node, n)

plot_DMinHeap_path(G, Gx, pos, start_node, end_node, n)
#from multiprocessing import Process
#p1 = Process(target=plot_DMinHeap, args=(G, Gx, pos, start_node, n))
#p2 = Process(target=plot_DFibHeap, args=(G, Gx, pos, start_node, n))
#p1.start()
#p2.start()
## and so on
#p1.join()
#p2.join()

