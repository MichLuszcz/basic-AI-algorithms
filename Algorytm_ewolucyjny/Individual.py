import numpy as np


# class holding a list describing the path taken as a list of city numbers
class Individual:
    def __init__(self, n_cities, path=None) -> None:
        if path:
            self.path = path
        else:
            self.path = np.random.choice(range(n_cities), n_cities, replace=False)

    def mutate(self, mutate_prob):
        # zamianki między miastami
        return self

    def __str__(self) -> str:
        return str(self.path)
