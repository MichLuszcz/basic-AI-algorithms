from Individual import Individual
import numpy as np
import copy as cp
from plotter import plot_path


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


# turniejowa reprodukcja,
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
    max_iterations = 500
    population = []
    pop_size = 300
    for _ in range(pop_size):
        population.append(Individual(len(cities)))
    # n_offsprings = len(population) // 2 # chyba nie potrzebne
    best_individual = find_best_individual(population)
    mutate_prob = 0.3
    # proces ewolucji:
    while current_iteration < max_iterations:
        new_population = reproduce(population)
        # mogę użyć reprodukcji turniejowej, czyli na każde miejsce losowane są dwa(lub więcej) osobniki i wybierany ten lepszy
        # powinna zwrócić nową populację (chyba tej samej wielkości),
        # ale prawdopodobieństwo powielenia starego osobnika do nowej
        # populacji jest proporcjonalne (lub odwrotnie proporcjonalne jesli przyjmiemy duży fitness jako zły)
        # do jego oceny funkcją fitness
        # UWAŻAĆ NA TO ŻEBY TEN SAM OBIEKT NIE BYŁ W WIELU MIEJSCACH NA RAZ BO BĘDĄ SIĘ WSZYSKIE MUTOWAŁY NARAZ
        mutated = mass_mutate(
            new_population, mutate_prob
        )  # tu mogą być krzyżowania ale chyba odpuszczę
        best_mutated = find_best_individual(mutated)
        if fitness(best_individual) < fitness(best_mutated):
            best_individual = best_mutated
        population = succession(population, mutated, fitness)
        current_iteration += 1
    print(best_individual)
    print(fitness(best_individual))
    plot_path(best_individual.path, cities)


if __name__ == "__main__":
    evolve()
