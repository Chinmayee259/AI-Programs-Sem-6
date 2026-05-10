# Simple Kruskal's Minimum Spanning Tree Algorithm

# Find parent
def find(parent, i):

    if parent[i] == i:
        return i

    return find(parent, parent[i])


# Kruskal Algorithm
def kruskal(V, edges):

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    parent = []

    for i in range(V):
        parent.append(i)

    print("\nEdge : Weight\n")

    count = 0
    index = 0

    while count < V - 1:

        u, v, w = edges[index]
        index += 1

        x = find(parent, u)
        y = find(parent, v)

        # If no cycle
        if x != y:

            print(u, "-", v, ":", w)

            parent[x] = y
            count += 1


# Driver Code

V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")

for i in range(E):

    u, v, w = map(int, input().split())

    edges.append([u, v, w])

kruskal(V, edges)


# Enter number of vertices: 5
# Enter number of edges: 7
# Enter edges (u v weight):
# 0 1 3
# 0 2 1
# 1 2 1
# 1 3 2
# 1 4 4
# 2 3 2
# 2 4 3

# Edge : Weight

# 0 - 2 : 1
# 1 - 2 : 1
# 1 - 3 : 2
# 2 - 4 : 3