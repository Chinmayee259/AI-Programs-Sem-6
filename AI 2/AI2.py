graph = {}

n = int(input("enter the number of the nodes : "))

for  i in range(n):
    node = input("enter the node : ")
    neighbours = input("enter the neighbour of the node(split by space : ").split()
    graph[node] = neighbours
    
visited = set()

def bfs(queue):
    if queue:
        node = queue.pop(0)
        if node not in visited:
            print(node,end = " ")
            visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
        bfs(queue)

start = input("enter the starting node : ")
queue = [start]

print("bfs traversal : ")
bfs(queue)
