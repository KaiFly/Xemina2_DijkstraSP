from Dijkstra_3a import *
from GraphDrawing import*
from test_complexity import gen_random_graph, gen_random_fullGraph
import matplotlib.pyplot as plt
import random 

G = Graph()
G.add_vertex('A')
G.add_vertex('B')
G.add_vertex('C')
G.add_vertex('D')
G.add_vertex('E')
G.add_vertex('F')
G.add_connection('A', 'B', 4)
G.add_connection('A', 'D', 1)
G.add_connection('A', 'C', 7)
G.add_connection('B', 'C', 2)
G.add_connection('C', 'E', 2)
G.add_connection('C', 'F', 3)
G.add_connection('D', 'B', 2)
G.add_connection('D', 'E', 4)
G.add_connection('E', 'B', 0.01)
G.add_connection('E', 'D', 3)
G.add_connection('F', 'E', 1)

return_from_Dijkstra_1 = Dijkstra_normal(G, 'A')
return_from_Dijkstra_2 = Dijkstra_MinHeap(G, 'A')
return_from_Dijkstra_3 = Dijkstra_FibHeap(G, 'A')

return_from_Dijkstra_1_path = Dijkstra_MinHeap(G, 'A', 'F')
l_path, path = Dijkstra_path(return_from_Dijkstra_1_path)

        # Test GraphDrawing.py
Drawing = Graph_Drawing(G)
plt.figure(1)
position = Drawing.draw_graph()
plt.figure(2)
Drawing.draw_path(path, position)
plt.title('SP length : ' +str(l_path)) 
#--------------------------------------------------------------------------------
G_large = gen_random_graph(30, 200)
v1 = random.choice(G_large.list_vertexes())
v2 = random.choice(G_large.list_vertexes())
return_from_Dijkstra_1_path = Dijkstra_MinHeap(G_large, v1, v2)
l_path, path = Dijkstra_path(return_from_Dijkstra_1_path)

Drawing = Graph_Drawing(G_large)
plt.figure(1)
position = Drawing.draw_graph()

plt.figure(2)
Drawing.draw_path(path, position)
plt.title('SP length '+v1+' to '+v2+' : '+str(l_path) +'\n'+'SP : '+str(path), loc = 'left')


