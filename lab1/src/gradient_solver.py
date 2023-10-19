from solver import Solver
from problem import Problem
from numpy import linalg
from copy import copy

DefaultBeta = 0.4
DefaultEpsilon = 0.05
MaxIterations = 150


class MinSolver(Solver):
    def __init__(self, beta=DefaultBeta, epsilon=DefaultEpsilon) -> None:
        self.beta = beta
        self.epsilon = epsilon

    def get_parameters(self):
        """Returns a dictionary of hyperparameters"""
        return {"beta": self.beta, "epsilon": self.epsilon}

    def solve(self, problem: Problem, x0: list, *args, **kwargs):
        """
        A method that solves the given problem for given initial solution.
        """
        # nazwy zmiennych
        current_point = x0
        visited_points = []
        # TODO zmienić na while loop
        iterations = 0
        # while visited_points < MaxIterations and
        for n in range(100):
            d = problem.gradient_value(x)
            if linalg.norm(d) <= self.epsilon:  # if close enough to local minimum, stop
                return current_point, visited_points
            visited_points.append(copy(x))

            for i in range(len(x)):
                x[i] -= self.beta * d[i]
        return x, visited_points
        # ma znalesc minimum
        # problem = funkcja i jej gradient
        # x0 = punkt startowy w n wymiarze
        #
