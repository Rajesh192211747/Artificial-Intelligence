def is_safe(board, row, col):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, row):
    n = len(board)

    # Base case: If all queens are placed
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col):
            # Place queen
            board[row][col] = 1

            # Recur to place rest of the queens
            if solve_queens(board, row + 1):
                return True

            # Backtrack if placing queen at board[row][col] doesn't lead to a solution
            board[row][col] = 0

    # If queen can't be placed in any column of this row, return False
    return False

def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))

def main():
    n = 8  # Board size
    board = [[0] * n for _ in range(n)]

    if solve_queens(board, 0):
        print("Solution:")
        print_solution(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
