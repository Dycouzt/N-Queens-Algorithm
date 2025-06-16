"""
This is the Exhaustive Search (DFS) algorithm script. The goal is to:
Place N queens on an N×N board such that:
- No two queens share the same row, column, or diagonal
- Recursive backtracking
- Tries every possibility (exponential complexity)
- Always finds all valid solutions (or the first if optimized)
"""
import time
import tracemalloc


def is_safe(queens, row, col):
    for r in range(row):
        c = queens[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def dfs(n, row=0, queens=None, solutions=None):
    if queens is None:
        queens = []
    if solutions is None:
        solutions = []

    if row == n:
        solutions.append(queens.copy())
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens.append(col)
            dfs(n, row + 1, queens, solutions)
            queens.pop()

def solve_n_queens_dfs(n):
    tracemalloc.start()
    start_time = time.time()

    solutions = []
    dfs(n, 0, [], solutions)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "n": n,
        "solutions_count": len(solutions),
        "execution_time": end_time - start_time,
        "peak_memory_kb": peak / 1024,
        "example_solution": solutions[0] if solutions else None
    }

# Example usage for quick testing
if __name__ == "__main__":
    result = solve_n_queens_dfs(8)
    print(f"N = {result['n']}")
    print(f"Solutions found: {result['solutions_count']}")
    print(f"Execution time: {result['execution_time']:.4f} seconds")
    print(f"Peak memory: {result['peak_memory_kb']:.2f} KB")
    print(f"Example solution: {result['example_solution']}")