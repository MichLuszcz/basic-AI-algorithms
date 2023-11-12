from Individual import Individual
import numpy as np


# the higher the fitness the better, so we assert the opposite of the path lenght
def fitness(individual: Individual, cities) -> float:
    path_lenght = 0.0
    path = np.array(individual.path)
    for i in range(len(individual.path) - 1):
        city1 = np.array(cities[path[i]])
        city2 = np.array(cities[path[i + 1]])
        path_lenght += np.linalg.norm(city2 - city1)
    return -path_lenght


# turniejowa reprodukcja,
def reproduce(population: list[Individual]):
    new_population = []
    for _ in range(len(population)):
        contender_1, contender_2 = np.random.choice(population, 2, replace=False)
        new_population.append(
            contender_1 if fitness(contender_1) > fitness(contender_2) else contender_2
        )
    return new_population


def mass_mutate(population: list[Individual]):
    for indivitual in population:
        indivitual.mutate()


def succession(
    population_1: list[Individual], population_2: list[Individual], fitness_funct
):
    all = population_1 + population_2
    all.sort(
        key=lambda x: fitness_funct(x), reverse=True
    )  # sort list in decending order by the opposite of the path's cost (big cost = low fitness),
    # so that low cost paths are in the front
    return all[: len(population_1)]


def 


def main():
    current_iteration = 0
    population = []
    n_offsprings = len(population) // 2
    best_individual = find_best(population)

    # proces ewolucji:

    new_population = reproduce(population)
    # mogę użyć reprodukcji turniejowej, czyli na każde miejsce losowane są dwa(lub więcej) osobniki i wybierany ten lepszy
    # powinna zwrócić nową populację (chyba tej samej wielkości),
    # ale prawdopodobieństwo powielenia starego osobnika do nowej
    # populacji jest proporcjonalne (lub odwrotnie proporcjonalne jesli przyjmiemy duży fitness jako zły)
    # do jego oceny funkcją fitness
    # UWAŻAĆ NA TO ŻEBY TEN SAM OBIEKT NIE BYŁ W WIELU MIEJSCACH NA RAZ BO BĘDĄ SIĘ WSZYSKIE MUTOWAŁY NARAZ
    mutated = mutate(new_population)  # tu mogą być krzyżowania ale chyba odpuszczę
    best_mutated = find_best(mutated)
    if fitness(best_individual) < fitness(best_mutated):
        best_individual = best_mutated
    population = succession(population, mutated, fitness)
