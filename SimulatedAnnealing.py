"""
This is the Simulated Annealing algorithm script.
- Like Hill Climbing, but occasionally allows “bad” moves (higher conflict) to escape local optimal
- The probability of accepting worse states decreases over time as the system “cools.”
"""
import random
import math
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

def random_neighbor(board):
    n = len(board)
    new_board = board[:]
    row = random.randint(0, n - 1)
    new_col = random.randint(0, n - 1)
    while new_col == new_board[row]:
        new_col = random.randint(0, n - 1)
    new_board[row] = new_col
    return new_board

def solve_n_queens_simulated_annealing(n, temperature=100.0, cooling_rate=0.99, max_steps=100000):
    tracemalloc.start()
    start_time = time.time()

    current = [random.randint(0, n - 1) for _ in range(n)]
    current_attacks = count_attacks(current)

    for step in range(max_steps):
        if current_attacks == 0:
            break

        neighbor = random_neighbor(current)
        neighbor_attacks = count_attacks(neighbor)
        delta = neighbor_attacks - current_attacks

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current = neighbor
            current_attacks = neighbor_attacks

        temperature *= cooling_rate
        if temperature < 1e-3:
            break

    end_time = time.time()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "n": n,
        "solution": current if current_attacks == 0 else None,
        "attacks": current_attacks,
        "execution_time": end_time - start_time,
        "peak_memory_kb": peak_mem / 1024
    }

# Example usage
if __name__ == "__main__":
    result = solve_n_queens_simulated_annealing(8)
    print(f"N = {result['n']}")
    if result["solution"]:
        print(f"Solution found: {result['solution']}")
    else:
        print("No solution found.")
    print(f"Execution time: {result['execution_time']:.4f} seconds")
    print(f"Peak memory: {result['peak_memory_kb']:.2f} KB")