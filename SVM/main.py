import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_moons, make_circles
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from SVM import SVM
import mnist
from plot import plot_svm

czumpi_array = mnist.test_images()

X1, y1 = make_blobs(n_samples=200, centers=2, cluster_std=0.60)
y1 = np.where(y1 <= 0, -1, 1)
print("First five rows and col values \nX1 : \n", X1[:5], " \n y1 :\n", y1[:5])
plt.scatter(X1[:, 0], X1[:, 1], c=y1, s=50, cmap='winter', alpha=.5)
plt.title("Dataset 1")
plt.show()

svm1 = SVM(0.01, 1)
w1, b1 = svm1.train(X1, y1, 0.001, 1000)
print("For dataset 1, score:", accuracy_score(svm1.predict(X1), y1))
plot_svm(X1, y1, w1, b1, title='Linear SVM for dataset 1')
