import csv
from ExhaustiveDFS import solve_n_queens_dfs
from HillClimbing import solve_n_queens_hill_climbing
from SimulatedAnnealing import solve_n_queens_simulated_annealing
from GeneticAlgorithm import solve_n_queens_genetic

Ns = [10, 30, 50, 100, 200]  # Sizes to test
results = []

def run_and_record(algorithm_name, solver_fn, n):
    print(f"Running {algorithm_name} for N = {n}...")
    result = solver_fn(n)

    # Handle possible solution key differences
    solution = result.get("solution") or result.get("example_solution")
    attacks = result.get("attacks", 0 if solution else "-")

    results.append({
        "Algorithm": algorithm_name,
        "N": result["n"],
        "Execution Time (s)": round(result["execution_time"], 4),
        "Memory Usage (KB)": round(result["peak_memory_kb"], 2),
        "Solution Found": "Yes" if solution else "No",
        "Attacks": attacks
    })

# Run tests
for n in Ns:
    if n <= 30:
        run_and_record("Exhaustive DFS", solve_n_queens_dfs, n)
    run_and_record("Hill Climbing", solve_n_queens_hill_climbing, n)
    run_and_record("Simulated Annealing", solve_n_queens_simulated_annealing, n)
    run_and_record("Genetic Algorithm", solve_n_queens_genetic, n)

# Write results to CSV
csv_file = "n_queens_comparison_results.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"\nComparison complete. Results saved to '{csv_file}'.")