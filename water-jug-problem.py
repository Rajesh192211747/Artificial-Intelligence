from collections import deque

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

    def __str__(self):
        return f"({self.jug1}, {self.jug2})"

    def is_goal(self, target):
        return self.jug1 == target or self.jug2 == target

    def successors(self, jug1_capacity, jug2_capacity):
        successors = []

        # Fill jug1
        successors.append(State(jug1_capacity, self.jug2))

        # Fill jug2
        successors.append(State(self.jug1, jug2_capacity))

        # Empty jug1
        successors.append(State(0, self.jug2))

        # Empty jug2
        successors.append(State(self.jug1, 0))

        # Pour from jug1 to jug2
        pour_amount = min(self.jug1, jug2_capacity - self.jug2)
        successors.append(State(self.jug1 - pour_amount, self.jug2 + pour_amount))

        # Pour from jug2 to jug1
        pour_amount = min(self.jug2, jug1_capacity - self.jug1)
        successors.append(State(self.jug1 + pour_amount, self.jug2 - pour_amount))

        return successors

def bfs(start_state, jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        current_state, path = queue.popleft()

        if current_state.is_goal(target):
            return path + [current_state]

        visited.add(current_state)

        for successor in current_state.successors(jug1_capacity, jug2_capacity):
            if successor not in visited:
                queue.append((successor, path + [current_state]))

    return None

def main():
    jug1_capacity = 4
    jug2_capacity = 3
    target = 2
    start_state = State(0, 0)

    solution = bfs(start_state, jug1_capacity, jug2_capacity, target)

    if solution:
        print("Solution found:")
        for state in solution:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
