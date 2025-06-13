"""
This is the Genetic algorithm Script. The goal is to:
Use a population of candidate solutions (boards).
- Evolve them over generations using:
- Selection (prefer better boards),
- Crossover (combine two parents),
- Mutation (introduce variation).
"""

import random
import time
import tracemalloc


def count_attacks(board):
    """Count number of attacking queen pairs."""
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def generate_board(n):
    """Generate a random board (one queen per row, unique column)."""
    board = list(range(n))
    random.shuffle(board)
    return board

def crossover(parent1, parent2):
    """Partially Mapped Crossover (PMX-like) to keep column uniqueness."""
    n = len(parent1)
    start = random.randint(0, n - 2)
    end = random.randint(start + 1, n - 1)
    child = [None] * n
    child[start:end+1] = parent1[start:end+1]

    p2_elements = [x for x in parent2 if x not in child[start:end+1]]
    idx = 0
    for i in range(n):
        if child[i] is None:
            child[i] = p2_elements[idx]
            idx += 1
    return child

def mutate(board, mutation_rate):
    """Swap two positions with given probability."""
    n = len(board)
    if random.random() < mutation_rate:
        i, j = random.sample(range(n), 2)
        board[i], board[j] = board[j], board[i]

def select_parents(population, fitnesses, elite_size):
    """Select parents using elitism and roulette-wheel selection."""
    sorted_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i])
    elite = [population[i] for i in sorted_indices[:elite_size]]
    total_fitness = sum(fitnesses)
    probabilities = [(total_fitness - f + 1) / (total_fitness + 1) for f in fitnesses]

    selected = random.choices(population, weights=probabilities, k=len(population) - elite_size)
    return elite + selected

def solve_n_queens_genetic(n, population_size=100, generations=1000, mutation_rate=0.01, elite_size=20):
    """Solve N-Queens using a Genetic Algorithm."""
    tracemalloc.start()
    start_time = time.time()

    population = [generate_board(n) for _ in range(population_size)]

    for gen in range(generations):
        fitnesses = [count_attacks(ind) for ind in population]

        if 0 in fitnesses:
            solution = population[fitnesses.index(0)]
            break

        population = select_parents(population, fitnesses, elite_size)

        next_gen = []
        for i in range(0, population_size, 2):
            parent1 = population[i]
            parent2 = population[(i + 1) % population_size]
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            next_gen.extend([child1, child2])

        population = next_gen[:population_size]
    else:
        # If loop completes with no solution
        solution = None

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "n": n,
        "solution": solution,
        "attacks": count_attacks(solution) if solution else -1,
        "execution_time": end_time - start_time,
        "peak_memory_kb": peak / 1024
    }

# Example usage
if __name__ == "__main__":
    result = solve_n_queens_genetic(8)
    print(f"N = {result['n']}")
    if result["solution"]:
        print(f"Solution found: {result['solution']}")
        print(f"Attacks: {result['attacks']}")
    else:
        print("No solution found.")
    print(f"Execution time: {result['execution_time']:.4f} seconds")
    print(f"Peak memory: {result['peak_memory_kb']:.2f} KB")
