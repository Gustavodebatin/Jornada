import random
import math

def function_to_optimize(x):
    result = 0
    for i in range(len(x) - 1):
        result += 100 * (x[i]**2 - x[i+1])**2 + (x[i] - 1)**2
    return result

def initialize_fireflies(num_fireflies, num_dimensions, bounds):
    fireflies = []
    for _ in range(num_fireflies):
        firefly = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(num_dimensions)]
        fireflies.append(firefly)
    return fireflies

def attractiveness(light_intensity_i, light_intensity_j, distance):
    beta = 1
    gamma = 0.05
    return beta * math.exp(-gamma * distance ** 2) * light_intensity_i

def distance(firefly_i, firefly_j):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(firefly_i, firefly_j)))

def move_firefly(firefly, best_firefly, step_size, bounds):
    new_firefly = firefly[:]
    for i in range(len(firefly)):
        new_firefly[i] += step_size * (best_firefly[i] - firefly[i]) + random.uniform(-1, 1)
        new_firefly[i] = max(min(new_firefly[i], bounds[i][1]), bounds[i][0])  # Manter dentro dos limites
    return new_firefly

def firefly_algorithm(num_fireflies, num_dimensions, bounds, max_generations):
    fireflies = initialize_fireflies(num_fireflies, num_dimensions, bounds)
    best_firefly = None
    best_intensity = float('inf')

    for generation in range(max_generations):
        for i in range(num_fireflies):
            intensity_i = function_to_optimize(fireflies[i])

            for j in range(num_fireflies):
                intensity_j = function_to_optimize(fireflies[j])
                if intensity_j < intensity_i:
                    distance_ij = distance(fireflies[i], fireflies[j])
                    attractiveness_ij = attractiveness(intensity_i, intensity_j, distance_ij)
                    step_size = 0.1
                    fireflies[i] = move_firefly(fireflies[i], fireflies[j], step_size, bounds)

            if intensity_i < best_intensity:
                best_intensity = intensity_i
                best_firefly = fireflies[i]

    return best_firefly, best_intensity

num_fireflies = 200
num_dimensions = 10
bounds = [(-100, 100) for _ in range(num_dimensions)]
max_generations = 100

best_solution, best_intensity = firefly_algorithm(num_fireflies, num_dimensions, bounds, max_generations)

print("Melhor solução encontrada:", best_solution)
print("Melhor intensidade encontrada:", best_intensity)

