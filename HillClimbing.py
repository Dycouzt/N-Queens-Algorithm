"""
This is the Hill Climbing algorithm script. The goal is to:
- Start with a random board (one queen per row, randomly placed).
- At each step, move a queen within its row to reduce the number of attacking pairs.
- If no better neighbor exists, it stops (may reach a local optimum).
"""
import random
import time
import tracemalloc


def count_attacks(board):
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def get_best_neighbor(board):
    n = len(board)
    best_board = board[:]
    min_attacks = count_attacks(board)

    for row in range(n):
        original_col = board[row]
        for col in range(n):
            if col == original_col:
                continue
            board[row] = col
            attacks = count_attacks(board)
            if attacks < min_attacks:
                min_attacks = attacks
                best_board = board[:]
        board[row] = original_col  # restore

    return best_board, min_attacks

def solve_n_queens_hill_climbing(n, max_restarts=100):
    tracemalloc.start()
    start_time = time.time()

    for _ in range(max_restarts):
        board = [random.randint(0, n - 1) for _ in range(n)]
        current_attacks = count_attacks(board)

        while True:
            neighbor, neighbor_attacks = get_best_neighbor(board)
            if neighbor_attacks >= current_attacks:
                break  # local optimum
            board = neighbor
            current_attacks = neighbor_attacks

        if current_attacks == 0:
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return {
                "n": n,
                "solution": board,
                "attacks": 0,
                "execution_time": end_time - start_time,
                "peak_memory_kb": peak / 1024
            }

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {
        "n": n,
        "solution": None,
        "attacks": -1,
        "execution_time": end_time - start_time,
        "peak_memory_kb": peak / 1024
    }

# Example usage
if __name__ == "__main__":
    result = solve_n_queens_hill_climbing(8)
    print(f"N = {result['n']}")
    if result["solution"]:
        print(f"Solution found: {result['solution']}")
    else:
        print("No solution found.")
    print(f"Execution time: {result['execution_time']:.4f} seconds")
    print(f"Peak memory: {result['peak_memory_kb']:.2f} KB")