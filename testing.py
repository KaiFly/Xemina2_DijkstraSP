# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:12:01 2019

@author: Kai
"""

import random
x = []
for i in range(10000000):
        10000<10000

min_val = float("INF")
for i in x :
        if i < min_val:
                min_val = i
                
dict_i = {}
A = ['a']*1000000
for i in range(1000000):
        dict_i[A[i]] = random.randint(0, 1000000)

min_val = float("INF")
for i in dict_i:
        if dict_i[i] < min_val :
                min_val = dict_i[i]
                v = i
min(dict_i.values())

# Test MPI

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1)
elif rank == 1:
    data = comm.recv(source=0)
    print('On process 1, data is ',data)


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


#import math
#import random
#import string
#num_ver = 1000
#num_edge = 1000*3
