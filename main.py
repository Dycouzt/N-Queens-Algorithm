"""
This is the main.py script that makes a simple and quick comparison of all the algorithms.
"""
from ExhaustiveDFS import solve_n_queens_dfs
from HillClimbing import solve_n_queens_hill_climbing
from SimulatedAnnealing import solve_n_queens_simulated_annealing
from GeneticAlgorithm import solve_n_queens_genetic

Ns = [10, 30, 50, 100, 200]

def run_quick_test(name, fn, n):
    print(f"\n{name} (N = {n})")
    result = fn(n)
    solution = result.get("solution") or result.get("example_solution")
    print(f"  ✓ Time:   {result['execution_time']:.4f} sec")
    print(f"  ✓ Memory: {result['peak_memory_kb']:.2f} KB")
    print(f"  ✓ Found:  {'Yes' if solution else 'No'}")

for n in Ns:
    print(f"\n=== Testing N = {n} ===")
    if n <= 30:
        run_quick_test("Exhaustive DFS", solve_n_queens_dfs, n)
    run_quick_test("Hill Climbing", solve_n_queens_hill_climbing, n)
    run_quick_test("Simulated Annealing", solve_n_queens_simulated_annealing, n)
    run_quick_test("Genetic Algorithm", solve_n_queens_genetic, n)
