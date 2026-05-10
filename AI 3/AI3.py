# AI 3. Implement A star Algorithm for 4-Queens problem.
import heapq


#Calculate number of conflicts
def heuristic(state):
        h = 0  # Start with 0 conflicts
        n = len(state)  # Number of queens placed so far

        for i in range(n): # Pick queens
            for j in range(i + 1, n): # Compare it with all queens after it. This avoids:comparing same pair twice, comparing queen with itself
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j): # Same column → conflict
                    # abs => abs(x) returns the positive value of a number
                    h += 1  # Increase conflict count
        return h

# A* algorithm
def a_star(n):
    #(f, g, state)
    pq = []
    heapq.heappush(pq, (0, 0, [])) #empty board

    while pq:
        f, g, state = heapq.heappop(pq)

        # Goal : all queens placed with no connflicts
        if len(state) == n and heuristic(state) == 0:   
            return state

        row = len(state)  #for row = 0 it means now we will keep a queen on row 0

        for col in range(n): #finding the column to place the queen
            new_state = state + [col] # create the new state list 
            h = heuristic(new_state)  #Check heuristic that is conflict if we place the queen at position (row,col)
            g_new = len(new_state)
            f_new = g_new + h

            heapq.heappush(pq, (f_new, g_new, new_state))  # Priority Queue is sorted by f value (smallest first)

    return None

n = 4
solution = a_star(n)

print("Solution (column positions) : ", solution)

if solution:
    print("\nBoard: ")
    for i in range(n):
            for j in range(n):
                if solution[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end = " ")
            print()
            