from numpy import euler_gamma, exp
from numpy import linspace, meshgrid
import matplotlib.pyplot as plt


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
    plt.show()


if __name__ == "__main__":
    graph_3d(funct2)
