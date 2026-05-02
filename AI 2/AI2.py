# AI 2. Implement Breadth First Search algorithm. Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.
def bfs_recursive(graph, queue, visited = None):
    if not queue:  #If the queue is empty, stop the function
        return
    node = queue.pop(0)
    print(node, end = " ")

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    
    bfs_recursive(graph, queue, visited)

def bfs(graph, start):
    visited = set([start])  # creates a set containing only the starting node.Mark the start node as already visited
    queue = [start]
    bfs_recursive(graph, queue, visited)



graph = {}

levels = int(input("\nEnter the number of levels : "))

for i in range(levels):
    n = int(input("\nEnter the number of nodes at level "+ str(i) + " : "))

    for j in range(n):
        node = input("Enter the node : ")
        children = input("Enter the children of node " + node + " (space separated): ").split()

        graph[node] = children

start = input ("\nEnter the starting node : ")
print("BFS : ", end = " ")
bfs(graph, start)
    


# --------------- OUTPUT ----------------------
# Enter the number of levels : 3

# Enter the number of nodes at level 0 : 1
# Enter the node : A
# Enter the children of node A (space separated): B C

# Enter the number of nodes at level 1 : 2
# Enter the node : B
# Enter the children of node B (space separated): D
# Enter the node : C
# Enter the children of node C (space separated): E

# Enter the number of nodes at level 2 : 2
# Enter the node : D
# Enter the children of node D (space separated): 
# Enter the node : E
# Enter the children of node E (space separated): 

# Enter the starting node : A
# BFS :  A B C D E 