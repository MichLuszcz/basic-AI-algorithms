from solver import Solver
from problem import Problem

DefaultBeta = 1.4

class GradientSolver(Solver):
    
    def __init__(self, beta = DefaultBeta) -> None:
        self.beta = beta
    
    def get_parameters(self):
        """Returns a dictionary of hyperparameters"""
        return {"beta": self.beta}

    
    def solve(self, problem: Problem, x0: list, *args, **kwargs):
        """
        A method that solves the given problem for given initial solution.
        It may accept or require additional parameters.
        Returns the solution and may return additional info.
        """
        x = x0
        while True:
            d = problem.gradient_value(x)
            for i in len(x):
                x[i] -= self.beta * d[i]
        # ma znalesc minimum
        # problem = funkcja i jej gradient
        # x0 = punkt startowy w n wymiarze
        #