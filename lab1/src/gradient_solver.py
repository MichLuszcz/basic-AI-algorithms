from solver import Solver
from problem import Problem

class GradientSolver(Solver):
    
    def get_parameters(self):
        """Returns a dictionary of hyperparameters"""
        ...
    
    def solve(self, problem: Problem, x0: tuple, *args, **kwargs):
        """
        A method that solves the given problem for given initial solution.
        It may accept or require additional parameters.
        Returns the solution and may return additional info.
        """
        ...
        x = x0
        while True:
            d = problem.gradient_value(x)
            x = x - 
        # ma znalesc minimum
        # problem = funkcja i jej gradient
        # x0 = punkt startowy w n wymiarze
        #