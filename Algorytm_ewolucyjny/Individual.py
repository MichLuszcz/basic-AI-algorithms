import numpy as np
import random as rand


# class holding a list describing the path taken as a list of city numbers
class Individual:
    def __init__(self, n_cities, path=None) -> None:
        if path:
            self.path = path
        else:
            self.path = np.random.choice(range(n_cities), n_cities, replace=False)

    def mutate(self, mutate_prob):
        # swap the order of visited cities
        for i in range(len(self.path)):
            if rand.random() < mutate_prob:
                j = np.random.choice(range(len(self.path)), 1, replace=False)
                self.path[i], self.path[j] = self.path[j], self.path[i]
        return self

    def __str__(self) -> str:
        return str(self.path)
