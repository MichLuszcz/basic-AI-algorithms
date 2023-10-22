from numpy import euler_gamma, exp
from numpy import linspace, meshgrid, arange
import matplotlib.pyplot as plt
from gradient_solver import MinSolver
from problem import Problem
import random


def funct1(x):
    return 1 / 4 * (x[0] ** 4)


def gradient1(x):
    return [x[0] ** 3]


def funct2(x):
    x1, x2 = x
    term1 = 1.5 - exp(-(x1**2) - x2**2)
    term2 = -0.5 * exp(-((x1 - 1) ** 2) - (x2 + 2) ** 2)
    return term1 + term2


def gradient2(x):
    return [
        2 * x[0] * exp(-x[0] ** 2 - x[1] ** 2)
        + (x[0] - 1) * exp(-((x[0] - 1) ** 2) - (x[1] + 2) ** 2),
        2 * x[1] * exp(-x[0] ** 2 - x[1] ** 2)
        + (x[1] - 1) * exp(-((x[0] - 1) ** 2) - (x[1] + 2) ** 2),
    ]


Graph_W = 5


def graph_3d(function):
    x = linspace(-Graph_W, Graph_W, 100)
    y = linspace(-Graph_W, Graph_W, 100)
    X, Y = meshgrid(x, y)
    Z = function([X, Y])

    fig = plt.figure(figsize=(15, 10))
    ax = plt.axes(projection="3d")

    ax.plot_surface(X, Y, Z, cmap="cool", alpha=0.8)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    ax.set_zlabel("z", fontsize=12)

    # plt.show()


def graph_path_3d(problem: Problem, solver: MinSolver, x0):
    # graph_3d(problem.function)
    x = linspace(-Graph_W, Graph_W, 100)
    y = linspace(-Graph_W, Graph_W, 100)
    X, Y = meshgrid(x, y)
    Z = problem.function([X, Y])

    fig = plt.figure(figsize=(15, 10))
    ax = plt.axes(projection="3d")

    ax.plot_surface(X, Y, Z, cmap="cool", alpha=0.5)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    ax.set_zlabel("z", fontsize=12)

    result = solver.solve(problem, x0)
    points = result[1]
    xs = []
    ys = []
    zs = []
    print(x0)
    # points = [[1, 1], [2, 2], [3, 5]]
    if points:
        for point in points:
            xs.append(point[0])
            ys.append(point[1])
            zs.append(problem.function_value(point))
        # print(xs)
    # ax = plt.axes(projection="3d")
    ax.scatter(xs, ys, zs, marker="o")
    ax.plot(xs, ys, zs, color="g")
    pass


def graph_path_2d(problem: Problem, solver: MinSolver, x0):
    X = linspace(-Graph_W, Graph_W, 50)
    Y = problem.function([X])
    # Y = X**2
    plt.figure(figsize=(14, 8))

    # plt.subplot(2, 3, 1)
    plt.plot(X, Y)
    plt.title("Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()

    result = solver.solve(problem, x0)
    points = result[1]
    xs = []
    ys = []
    print(x0)
    # points = [[1, 1], [2, 2], [3, 5]]
    if points:
        for point in points:
            xs.append(point[0])
            ys.append(problem.function_value(point))
    plt.scatter(xs, ys, marker="o")
    plt.plot(xs, ys, color="g")


if __name__ == "__main__":
    # graph_3d(funct2)
    # random_x = random.uniform(-3, 3)
    # random_y = random.uniform(-3, 3)
    # x0 = [random_x, random_y]
    beta = 0.08
    epsilon = 0.04
    solver = MinSolver(beta, epsilon)
    problem = Problem(funct1, gradient1)
    # graph_path_3d(problem, solver, x0)
    x0 = [5]
    graph_path_2d(problem, solver, x0)
    plt.title(f"beta: {beta}, epsilon: {epsilon}, pkt start: {x0}")
    plt.show()
