from graph import Graph, Dijkstra_greedy, Dijkstra_MinHeap
import random
import string
import math
import time 
from numpy.random import seed 
from numpy.random import randint 
import matplotlib.pyplot as plt

def gen_random_graph(num_ver, num_edge):
        Gr = Graph()
        len_s_max = int(math.log(num_ver, 26)) + 1
        l = []
        while(True):
                s = ''
                for i in range(len_s_max):
                        s1 = random.choice(string.ascii_uppercase)
                        s += s1
                if(s in l):
                        continue
                l.append(s)
                Gr.add_vertex(s)
                if len(l) == num_ver :
                        break
        for j in range(num_edge):
                start = random.choice(Gr.list_vertexes())
                while(True):
                        end = random.choice(Gr.list_vertexes())
                        if end != start :
                                break
                weights = random.randint(1, 10)
                Gr.add_connection(start, end, weights)
        return Gr

def gen_random_fullGraph(num_ver):
        Gr = Graph()
        len_s_max = int(math.log(num_ver, 26)) + 1
        l = []
        while(True):
                s = ''
                for i in range(len_s_max):
                        s1 = random.choice(string.ascii_uppercase)
                        s += s1
                if(s in l):
                        continue
                l.append(s)
                Gr.add_vertex(s)
                if len(l) == num_ver :
                        break
        for start in Gr.list_vertexes():
                for end in Gr.list_vertexes():
                        if end == start:
                                continue
                        weights = random.randint(1, 10)
                        Gr.add_connection(start, end, weights)
        return Gr
Gr = gen_random_graph(1000, 20000)
Gr2 = gen_random_fullGraph(1000)
#def calculate_time(func): 
#        def inner1(*args, **kwargs): 
#                begin = time.time() 
#          
#                func(*args, **kwargs) 
#  
#                end = time.time() 
#        print("Total time taken in : ", func.__name__, end - begin) 
#  
#    return inner1 
def run_testing(funct):
        def inner(*args, **kwargs):
                number_ver = list()
                times = list()
                for i in range(0, 10): 
                        a = (i + 1)*50
                        Grx = gen_random_fullGraph(a)
                        Verx = random.choice(Grx.list_vertexes())
                        start = time.process_time()
#                        Dijkstra_greedy(Grx, Verx)
                        funct(*args, **kwargs)
                        end = time.process_time()
                        print(a, "Number of vertexes in graph : ", end-start) 
                        number_ver.append(a) 
                        times.append(end-start)
                return number_ver, times
        return inner
plt.xlabel('Number of vertexes') 
plt.ylabel('Time Complexity')
number_ver1
plt.plot(number_ver, times, color ='red', label ='Dijkstra Normal - Dijkstra MinHeap') 
plt.grid() 
plt.legend() 
plt.show() 