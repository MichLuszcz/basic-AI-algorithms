from Individual import Individual
import numpy as np
import copy as cp
from plotter import plot_path, plot_data


cities = [
    [35, 51],
    [113, 213],
    [82, 280],
    [322, 340],
    [256, 352],
    [160, 24],
    [322, 145],
    [12, 349],
    [282, 20],
    [241, 8],
    [398, 153],
    [182, 305],
    [153, 257],
    [275, 190],
    [242, 75],
    [19, 229],
    [303, 352],
    [39, 309],
    [383, 79],
    [226, 343],
]


# the higher the fitness the better, so we assert the opposite of the path lenght
def fitness(individual: Individual) -> float:
    path_lenght = 0.0
    path = np.array(individual.path)
    for i in range(len(individual.path) - 1):
        city1 = np.array(cities[path[i]])
        city2 = np.array(cities[path[i + 1]])
        path_lenght += np.linalg.norm(city2 - city1)
    city1 = np.array(cities[path[0]])
    city2 = np.array(cities[path[-1]])
    path_lenght += np.linalg.norm(city2 - city1)
    return -path_lenght


# tourney reproduction
def reproduce(population: list[Individual]):
    new_population = []
    for _ in range(len(population)):
        contender_1, contender_2 = np.random.choice(population, 2, replace=False)
        new_population.append(
            cp.deepcopy(contender_1)
            if fitness(contender_1) > fitness(contender_2)
            else cp.deepcopy(contender_2)
        )
    return new_population


def mass_mutate(population: list[Individual], mutate_prob):
    for indivitual in population:
        indivitual.mutate(mutate_prob)
    return population


def succession(
    population_1: list[Individual], population_2: list[Individual], fitness_funct
):
    all = population_1 + population_2
    all.sort(
        key=lambda x: fitness_funct(x), reverse=True
    )  # sort list in decending order by the opposite of the path's cost (big cost = low fitness),
    # so that low cost paths are in the front
    return all[: len(population_1)]


def find_best_individual(population: list[Individual]):
    best_ind = population[0]
    best_fitness = fitness(best_ind)
    for individual in population:
        indv_fitness = fitness(individual)
        if indv_fitness > best_fitness:
            best_fitness = indv_fitness
            best_ind = individual
    return best_ind


def evolve():
    current_iteration = 0
    max_iterations = 10
    pop_size = 100
    mutate_prob = 0.3
    population = []
    best_values = []
    for _ in range(pop_size):
        population.append(Individual(len(cities)))
    best_individual = find_best_individual(population)
    best_individual_value = fitness(best_individual)
    # evolutionary process:
    while current_iteration < max_iterations:
        best_values.append(best_individual_value)
        new_population = reproduce(population)
        mutated = mass_mutate(new_population, mutate_prob)
        best_mutated = find_best_individual(mutated)
        best_mutated_value = fitness(best_mutated)
        if best_individual_value < best_mutated_value:
            best_individual = best_mutated
            best_individual_value = best_mutated_value
        population = succession(population, mutated, fitness)
        current_iteration += 1
    print(best_individual)
    print(best_individual_value)
    plot_data(best_values, max_iterations, pop_size, mutate_prob)
    plot_path(
        best_individual.path,
        cities,
        round(best_individual_value, 2),
        max_iterations,
        pop_size,
        mutate_prob,
    )


if __name__ == "__main__":
    evolve()
