#Write the python program to solve 8-Puzzle problem 
import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.calculate_cost()

    def __lt__(self, other):
        return self.cost < other.cost

    def calculate_cost(self):
        return self.depth + self.heuristic()

    def heuristic(self):
        # Manhattan distance heuristic
        total_cost = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    row = (self.state[i][j] - 1) // 3
                    col = (self.state[i][j] - 1) % 3
                    total_cost += abs(row - i) + abs(col - j)
        return total_cost

    def generate_children(self):
        children = []
        zero_row, zero_col = self.find_zero_position()

        # Possible moves: Up, Down, Left, Right
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in moves:
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [row[:] for row in self.state]
                new_state[zero_row][zero_col], new_state[new_row][new_col] = \
                    new_state[new_row][new_col], new_state[zero_row][zero_col]
                children.append(PuzzleNode(new_state, self, (dr, dc), self.depth + 1))

        return children

    def find_zero_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def get_path(self):
        path = []
        current = self
        while current is not None:
            path.append((current.state, current.move))
            current = current.parent
        path.reverse()
        return path

def solve_8_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    frontier = [initial_node]
    explored = set()

    while frontier:
        current_node = heapq.heappop(frontier)

        if current_node.state == goal_state:
            return current_node.get_path()

        explored.add(tuple(map(tuple, current_node.state)))

        for child in current_node.generate_children():
            if tuple(map(tuple, child.state)) not in explored:
                heapq.heappush(frontier, child)

    return None

# Example initial and goal states
initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

solution = solve_8_puzzle(initial_state)
if solution:
    print("Solution found!")
    for step, move in solution:
        print(step)
        print("Move:", move)
        print()
else:
    print("No solution found.")
    
    
