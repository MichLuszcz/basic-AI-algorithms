from problem import Problem
from gradient_solver import MinSolver
from numpy import euler_gamma


def main():
    solver = MinSolver(0.2)

    def square_funct(x):
        return 1 / 4 * (x[0] ** 4)

    def gradient(x):
        return [x[0] ** 3]

    problem = Problem(square_funct, gradient)
    print(solver.solve(problem, [2]))


if __name__ == "__main__":
    main()
