import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=0, g=0, h=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = divmod(goal.index(value), 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def get_neighbors(state):
    neighbors = []
    zero_position = [(i, row.index(0)) for i, row in enumerate(state) if 0 in row][0]
    x, y = zero_position

    moves = [
        (x-1, y),
        (x+1, y),
        (x, y-1),
        (x, y+1)
    ]

    for new_x, new_y in moves:
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, PuzzleState(start, g=0, h=manhattan_distance(start, sum(goal, []))))
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.board == goal:
            path = []
            while current_state:
                path.append(current_state.board)
                current_state = current_state.parent
            return path[::-1]

        closed_set.add(tuple(map(tuple, current_state.board)))

        for neighbor in get_neighbors(current_state.board):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple in closed_set:
                continue

            g_cost = current_state.g + 1
            h_cost = manhattan_distance(neighbor, sum(goal, []))
            neighbor_state = PuzzleState(neighbor, parent=current_state, g=g_cost, h=h_cost)
            heapq.heappush(open_list, neighbor_state)

    return None

def print_board(state):
    for row in state:
        print(row)
    print()

start = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = a_star(start, goal)

if solution:
    print("Solution found in", len(solution) - 1, "moves!")
    for step in solution:
        print_board(step)
else:
    print("No solution found.")
