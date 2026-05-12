graph = {}

n = int(input("enter the number of the nodes : "))

for  i in range(n):
    node = input("enter the node : ")
    neighbours = input("enter the neighbour of the node(split by space : ").split()
    graph[node] = neighbours
    
visited = set()

def dfs(node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)

start = input("enter the starting node : ")
print("dfs traversal : ")
dfs(start)
