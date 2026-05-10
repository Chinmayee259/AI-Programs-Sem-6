# implement Greedy search algorithm for the following application Prim's Minimal Spanning Tree Algorithm & Kruskal's Minimal Spanning Tree Algorithm.

def prim_mst(graph):
    INF = 9999999
    V = len(graph) # Number of rows in graph

    selected = [False] * V  # Created a list of size V i.e. 5 and put False at every index
    # This list is to keep track of all the visited nodes 
    selected[0] = True   # selected the 0 node

    print("Edge : Weight")

    for i in range (V-1):   # If the graph has V vertices then the MST must have the V-1 edges 
        minimum = INF
        x = 0
        y = 0

        for j in range (V): #This is to check all the other selected nodes
            if selected[j]: # If the node is visited then 

                for k in range(V):  # Check of its adjacent
                    if (not selected[k] and graph[j][k]): # if that adjacent node is not visited and if there is a connection then 
                        if minimum > graph[j][k]:   # if min > their distance then
                            minimum = graph[j][k]   # its the minimum weight
                            x = j   
                            y = k

        print(x, "-", y, ":", graph[x][y]) # Print

        selected[y] = True   # mark as visited




# adjacency matrix showing the edge weight between the nodes
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

prim_mst(graph)