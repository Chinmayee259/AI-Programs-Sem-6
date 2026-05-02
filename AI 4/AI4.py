# AI 4. Implement A star Algorithm for 8-Puzzle problem.

import heapq

#goal state
goal = [[1,2,3],
        [4,5,6],
        [7,8,9]]

def to_tuple(state):
    return tuple(tuple(row) for row in state)

    # tuple(row) for row in state => Converts each row into tuple:
    # tuple(tuple(row) for row in state) => Wrap everything into one tuple
    # e.g. visited = ((1, 2, 3),
                    #   (4, 0, 6),
                    #   (7, 5, 8))
    
def a_star(start):
    pq = []
    heapq.heappush(pq, (0, 0, start))

    visited = set()

    while pq:
        f, g, state = heapq.heappop(pq)

        if state == goal:
            return state
        
        visited.add(to_tuple(state))

        for neighbor in get_neighbors(state):
            if



start = []
print("Enter initial 3 * 3 puzzle (use 0 for blank. Separate numbers by space. Press Enter to change the row) : ")
for i in range(3):
    row = list(map(int, input().split())) 
    # input().split()  => take input as string e.g. 1 2 3 and then split it by space . ['1', '2', '3']
    # (map(int, input().split())  => convert the string into int [1, 2, 3]
    # list is a built-in data type
    start.append(row)

# run A*
result = a_star(start)




