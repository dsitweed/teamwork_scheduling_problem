import random
import numpy as np

# Define the data
requests = [
    {'id': 1, 'start': 1, 'end': 4},
    {'id': 2, 'start': 2, 'end': 5},
    {'id': 3, 'start': 3, 'end': 6},
    {'id': 4, 'start': 5, 'end': 7},
    {'id': 5, 'start': 6, 'end': 8},
    {'id': 6, 'start': 7, 'end': 9},
    {'id': 7, 'start': 8, 'end': 10},
    {'id': 8, 'start': 9, 'end': 11},
    {'id': 9, 'start': 10, 'end': 12},
    {'id': 10, 'start': 11, 'end': 13}
]
num_slots = 2

# GA Parameters
population_size = 10
generations = 20
mutation_rate = 0.1

# ACO Parameters
pheromone_evaporation = 0.5
pheromone_deposit = 1.0

# Initialize population
def initialize_population(num_requests, num_slots):
    return [[random.randint(0, num_slots - 1) for _ in range(num_requests)] for _ in range(population_size)]

# Calculate fitness
def calculate_fitness(schedule):
    conflicts = 0
    for j in range(num_slots):
        slot_requests = [requests[i] for i in range(len(schedule)) if schedule[i] == j]
        for i in range(len(slot_requests)):
            for k in range(i + 1, len(slot_requests)):
                if not is_non_conflicting(slot_requests[i], slot_requests[k]):
                    conflicts += 1
    return -conflicts

# Non-conflicting check
def is_non_conflicting(req1, req2):
    return req1['end'] <= req2['start'] or req2['end'] <= req1['start']

# GA operations
def select_parents(population):
    sorted_pop = sorted(population, key=calculate_fitness)
    return sorted_pop[:2]  # Simple selection of best two

def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(schedule):
    for i in range(len(schedule)):
        if random.random() < mutation_rate:
            schedule[i] = random.randint(0, num_slots - 1)
    return schedule

# ACO operations
def update_pheromone(pheromone_matrix, best_schedule):
    # For simplicity, updating pheromone based on best schedule
    for i, slot in enumerate(best_schedule):
        pheromone_matrix[i][slot] += pheromone_deposit
    return pheromone_matrix

def ant_colony_optimization():
    pheromone_matrix = np.ones((len(requests), num_slots))
    for _ in range(generations):
        population = initialize_population(len(requests), num_slots)
        best_schedule = max(population, key=lambda s: calculate_fitness(s))

        # Update pheromone
        pheromone_matrix = update_pheromone(pheromone_matrix, best_schedule)

        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

        population = new_population

    # Return best schedule
    return best_schedule

# Run the optimization
best_schedule = ant_colony_optimization()

# Output the result
for j in range(num_slots):
    print(f"Slot {j + 1} assignments:")
    for i in range(len(best_schedule)):
        if best_schedule[i] == j:
            print(f"  Request {requests[i]['id']} from {requests[i]['start']} to {requests[i]['end']}")
