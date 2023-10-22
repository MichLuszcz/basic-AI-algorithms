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
        current_coordinates = x0
        visited_points = []
        iterations = 0
        gradient_value = problem.gradient_value(current_coordinates)
        # if close enough to local minimum or takes too long, stop
        while iterations < MaxIterations and linalg.norm(gradient_value) > self.epsilon:
            iterations += 1
            visited_points.append(
                copy(current_coordinates)
            )  # add current point to the list of visited points
            for i in range(len(current_coordinates)):
                current_coordinates[i] -= (
                    self.beta * gradient_value[i]
                )  # move the point in the decending direction
            gradient_value = problem.gradient_value(current_coordinates)
        visited_points.append(current_coordinates)  # add the last visited point
        return current_coordinates, visited_points
        # ma znalesc minimum
        # problem = funkcja i jej gradient
        # x0 = punkt startowy w n wymiarze
        #
