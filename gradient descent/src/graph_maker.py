from numpy import exp
from numpy import linspace, meshgrid, average
import matplotlib.pyplot as plt
from gradient_solver import MinSolver
from problem import Problem
import random
import statistics as stat


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

    plt.figure(figsize=(15, 10))
    ax = plt.axes(projection="3d")

    ax.plot_surface(X, Y, Z, cmap="cool", alpha=0.8)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    ax.set_zlabel("z", fontsize=12)


def graph_path_3d(problem: Problem, solver: MinSolver, x0):
    x = linspace(-Graph_W, Graph_W, 100)
    y = linspace(-Graph_W, Graph_W, 100)
    X, Y = meshgrid(x, y)
    Z = problem.function([X, Y])

    plt.figure(figsize=(15, 10))
    ax = plt.axes(projection="3d")

    ax.plot_surface(X, Y, Z, cmap="cool", alpha=0.5)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    ax.set_zlabel("z", fontsize=12)
    plt.title(f"beta: {solver.beta}, epsilon: {solver.epsilon}, pkt start: {x0}")

    result = solver.solve(problem, x0)
    points = result[1]
    xs = []
    ys = []
    zs = []
    print(x0)
    if points:
        for point in points:
            xs.append(point[0])
            ys.append(point[1])
            zs.append(problem.function_value(point))
    ax.scatter(xs, ys, zs, marker="o")
    ax.plot(xs, ys, zs, color="g")
    pass


def graph_path_2d(problem: Problem, solver: MinSolver, x0):
    X = linspace(-Graph_W, Graph_W, 50)
    Y = problem.function([X])
    plt.figure(figsize=(14, 8))

    plt.plot(X, Y)
    plt.title("Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid()
    plt.title(f"beta: {solver.beta}, epsilon: {solver.epsilon}, pkt start: {x0}")

    result = solver.solve(problem, x0)
    points = result[1]
    xs = []
    ys = []
    if points:
        for point in points:
            xs.append(point[0])
            ys.append(problem.function_value(point))
    plt.scatter(xs, ys, marker="o")
    plt.plot(xs, ys, color="g")


def random_tests_2d():
    beta = 0.079
    epsilon = 4
    solver = MinSolver(beta, epsilon)
    problem = Problem(funct1, gradient1)
    steps_taken = []
    final_values = []
    for _ in range(100):
        x0 = [random.uniform(-5, 5)]
        result = solver.solve(problem, x0)
        last_point = result[0]
        steps_taken.append(len(result[1]) - 1)
        final_values.append(problem.function_value(last_point))
    print(f"standard deviation: {stat.stdev(final_values)}")
    print(f"average result: {average(final_values)}")
    print(f"avg amount of steps: {average(steps_taken)}")
    print(f"std dev of steps: {stat.stdev(steps_taken)}")
    graph_path_2d(problem, solver, x0)
    plt.title(f"beta: {beta}, epsilon: {epsilon}, pkt start: {x0}")


def random_tests_3d():
    beta = 0.7
    epsilon = 0.01
    solver = MinSolver(beta, epsilon)
    problem = Problem(funct2, gradient2)
    steps_taken = []
    final_values = []
    for i in range(100):
        random_x = random.uniform(-4, 4)
        random_y = random.uniform(-4, 4)
        x0 = [random_x, random_y]
        result = solver.solve(problem, x0)
        last_point = result[0]
        steps_taken.append(len(result[1]) - 1)
        final_values.append(problem.function_value(last_point))

    print(f"standard deviation: {stat.stdev(final_values)}")
    print(f"average result: {average(final_values)}")
    print(f"avg amount of steps: {average(steps_taken)}")
    print(f"std dev of steps: {stat.stdev(steps_taken)}")
    plt.title(f"beta: {beta}, epsilon: {epsilon}, pkt start: {x0}")


if __name__ == "__main__":
    random_x = random.uniform(-2, 2)
    random_y = random.uniform(-2, 2)
    x0 = [3.3, -1.7]
    beta = 1
    epsilon = 0.00001
    solver = MinSolver(beta, epsilon)
    # graph_path_2d(Problem(funct1, gradient1), solver, x0)
    graph_path_3d(Problem(funct2, gradient2), solver, x0)
    plt.show()
    # random_tests_3d()
