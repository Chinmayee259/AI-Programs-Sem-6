# MST using Prims's Algorithm

import heapq


V = int(input("Enter the number of vertices : "))
E = int(input("Enter the number of edges : "))

graph = {}
for i in range(V): # This loop creates an empty list for every vertex (node) in the graph.
    graph[i] = [] 

print("Enter edges (u v weight): ") 

# Takes E edges as input and stores them in the graph (adjacency list).
for x in range(E):
    u, v, w = map(int)
