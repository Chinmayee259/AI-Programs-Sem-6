import heapq

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

def h(board): # It calculates Manhattan Distance heuristic
    dist = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            dist += abs(x - i) + abs(y - j)
    return dist

def find_zero(board): # It finds the position (row, column) of the blank tile (0) in the 8-puzzle board.
    for i in range(3): # Loops through rows (0, 1, 2)
        for j in range(3): # Loops through columns (0, 1, 2)
            if board[i][j] == 0: # Checks: “Is this cell the blank tile?”
                return i, j # returns its position (row, column)
            
def to_tuple(board):
    return tuple(tuple(row) for row in board)
    # tuple(row) for row in board => converts each row list → tuple
    # tuple(...) => converts all rows into one big tuple

def solve(start):
    pq = []
    heapq.heappush(pq, (h(start), 0, start))  # This line inserts the initial board into the priority queue with its heuristic value and cost 0.”

    visited = set()

    while pq:
        f, g, board = heapq.heappop(pq)

        if board == goal:
            print("\nGoal Reached!")
            for row in board:
                print(row)
            return
        
        visited.add(to_tuple(board))  # It stores the current board state in the visited set as a tuple

        x, y = find_zero(board) # It finds the position (row, column) of the blank tile (0) in the board. To generate new states, we must know:Where is 0?
        # Example: 0 is at position → (1, 2) So:x = 1 , y = 2

        moves = [(1,0), (-1, 0), (0, 1), (0, -1)]  # This list represents all possible directions in which the blank tile (0) can move.
        # Meaning: (1, 0) Down Row +1, (-1, 0) Up Row -1, (0, 1) Right Column +1, (0, -1) Left Column -1

        for dx, dy in moves: # It tries all possible moves (up, down, left, right) from the current position of 0. Takes one direction at a time from moves
            nx, ny = x + dx, y + dy # New row and column position

            if 0 <= nx < 3 and 0 <= ny < 3:  # This checks if the new position is inside the 3×3 board
                new_board = [row[:] for row in board]  # This creates a deep copy of the board
                # row[:] → copies each row
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                #it swaps the blank tile (0) with a neighboring tile. This creates a new puzzle state

                t = to_tuple(new_board) # It converts the new board (2D list) into a tuple and stores it in t.
                
                if t not in visited:
                    heapq.heappush(pq, (g+1+h(new_board), g+1, new_board))
                    # We add 1 to g because we take one move, and then add heuristic to get total estimated cost. New cost = previous cost + move + heuristic




print("Enter the initial state row-wise (use 0 for blanck) : ")

start = []
for i in range(3):
    row = list(map(int, input("Row" + str(i) + " : ").split()))
    start.append(row)

solve(start)