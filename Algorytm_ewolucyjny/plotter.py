import matplotlib.pyplot as plt
import numpy as np


def plot_path(route, cities):
    cities = np.array(cities)
    plt.figure(figsize=(12, 8))
    plt.scatter(x=cities[:, 0], y=cities[:, 1], s=1000, zorder=1)
    for i in range(len(cities)):
        plt.text(
            cities[i][0],
            cities[i][1],
            str(i),
            horizontalalignment="center",
            verticalalignment="center",
            size=16,
            c="white",
        )
    for i in range(len(route)):
        plt.plot(
            [cities[route[i]][0], cities[route[(i + 1) % len(route)]][0]],
            [cities[route[i]][1], cities[route[(i + 1) % len(route)]][1]],
            "k",
            zorder=0,
        )
    if len(route) > 0:
        plt.title(f"Visiting {len(route)} cities in length", size=16)
    else:
        plt.title(f"{len(cities)} cities", size=16)
    plt.show()


def plot_data(best_vals, average_vals=None):
    if average_vals:
        if not len(best_vals) == len(average_vals):
            raise ValueError("Values to plot have to be the same in size.")
    x_vals = np.arange(len(best_vals))
    ax = plt.subplot()
    ax.plot(x_vals, best_vals, color="r", label="Best specimen in each epoch")
    if average_vals is not None:
        ax.plot(x_vals, average_vals, color="b", label="Average specimen in each epoch")
        ax.set_title("Best and average values of the goal function in each epoch")
    else:
        ax.set_title("Best value of the goal function in each epoch")
    plt.grid(True)
    plt.legend()
    plt.show()
