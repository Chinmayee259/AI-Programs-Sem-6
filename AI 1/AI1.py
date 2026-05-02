# AI 1. Implement Depth First Search algorithm. Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.

# ------------ DFS --------------------------
def dfs(graph, node, visited = None):   #visited = None is used so that a **new visited set is created only once (at the first call) and safely shared                                  across recursive calls without default mutable bugs.
    if visited is None:
        visited = set()
    print(node, end=" ")
    visited.add(node)

    for neighbor in graph.get(node, []): #graph.get(node, []) returns the value of node (its neighbors), and if the node is not present, it returns an empty list [] instead of giving an error.
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# ------------ INPUT --------------------------
graph = {}

levels = int(input("Enter number of levels : "))

for i in range(levels):
    n = int(input("\nEnter number of nodes at level " + str(i) + ": "))

    for j in range(n):
        node = input("Enter node : ")
        children = input("Enter children of "+ node + " (space separated) : ").split()

        graph[node] = children

start = input("\n Enter the starting node : ")

print("DFS : ", end=" ")
dfs(graph, start)


# ------------ OUTPUT --------------------------
# Enter number of levels: 3

# Enter number of nodes at level 0: 1
# Enter node: A
# Enter children of A (space separated): B C

# Enter number of nodes at level 1: 2
# Enter node: B
# Enter children of B (space separated): D
# Enter node: C
# Enter children of C (space separated): E

# Enter number of nodes at level 2: 2
# Enter node: D
# Enter children of D (space separated): 
# Enter node: E
# Enter children of E (space separated): 

# Enter starting node: A
# DFS :  A B D C E 