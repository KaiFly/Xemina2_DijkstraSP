from Dijkstra_3a import Graph, Dijkstra_MinHeap, Dijkstra_FibHeap, Dijkstra_normal
import random
import string
import math
import time 
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

def run_testing(key_Grtype : int, n = 5, step = 200):
        number_ver = list()
        time1 = list()
        time2 = list()
        time3 = list()
        for i in range(0, n): 
                a = (i + 1)*step
                if key_Grtype == 1:
                        print("Randomizing full graph ...")
                        num_ver = a
                        Grx = gen_random_fullGraph(num_ver)
                        Verx = random.choice(Grx.list_vertexes())
                        gr = 'full graph'
                elif key_Grtype >= 2 :
                        print("Randomizing spare graph ...")
                        num_ver = a
                        num_edge = int(a*(a-1)/8)
                        Grx = gen_random_graph(num_ver, num_edge)
                        Verx = random.choice(Grx.list_vertexes())                    
                        gr = 'parse graph'
                print("Done.")
                start1 = time.process_time()
                Dijkstra_normal(Grx, Verx)
                end1 = time.process_time()
                print(num_ver, "Dijkstra Normal Numb of vertexes in " + gr + " : ", end1-start1) 
                start2 = time.process_time()
                Dijkstra_MinHeap(Grx, Verx)
                end2 = time.process_time()
                print(num_ver, "Dijkstra MinHeap Numb of vertexes in " + gr + " : ", end2-start2) 
                start3 = time.process_time()
                Dijkstra_FibHeap(Grx, Verx)
                end3 = time.process_time()
                print(num_ver, "Dijkstra FibHeap Numb of vertexes in " + gr + " : ", end3-start3) 
                number_ver.append(a)
                time1.append(end1-start1)
                time2.append(end2-start2)
                time3.append(end3-start3)
        return number_ver, time1, time2, time3

if __name__ == "__main__":
        #key_Grtype : 1 - full graph ; 2 - parse graph (number of edge = 1/4 max(edges))
        number_ver, time_1, time_2, time_3 = run_testing(key_Grtype = 1, n = 10, step = 100)
        
        plt.xlabel('Number of vertexes') 
        plt.ylabel('Time Complexity')
        
        plt.plot(number_ver, time_1, color ='red', label ='Dijkstra Normal')
        plt.plot(number_ver, time_2, color ='blue', label ='Dijkstra MinHeap')
        plt.plot(number_ver, time_3, color ='yellow', label ='Dijkstra FibHeap')
        plt.grid()
        plt.legend() 
        plt.show() 