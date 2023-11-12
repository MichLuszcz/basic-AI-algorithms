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
