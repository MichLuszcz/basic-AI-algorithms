from problem import Problem
from gradient_solver import MinSolver
from graph_maker import funct2, gradient2


def main():
    solver = MinSolver(0.1, 0.001)

    def square_funct(x):
        return 1 / 4 * (x[0] ** 4)

    def gradient(x):
        return [x[0] ** 3]

    problem = Problem(funct2, gradient2)
    print(solver.solve(problem, [1, -2.5]))


if __name__ == "__main__":
    main()
