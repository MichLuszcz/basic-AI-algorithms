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

svms = []
for i in range(10):
    svms.append(SVM(0.01, i))

print("Training for minst database:")
training_set, training_labels = mnist.train_images()[:300], mnist.train_labels()[:300]
training_set = training_set.reshape(training_set.shape[0], -1) / 255.0

testing_set = mnist.test_images()[:100]
testing_set = testing_set.reshape(testing_set.shape[0], -1) / 255.0
testing_labels = mnist.test_labels()[:100]

print(training_set[0])
for svm in svms:
    svm.train(training_set, training_labels, 0.001, 2000)

total_found = 0
for sample_index in range(testing_set.shape[0]):
    found = -1
    recognised = []
    for svm_index in range(10):
        result = svms[svm_index].predict(testing_set[sample_index])
        if result == 1 and svm_index == testing_labels[sample_index]:
            found = svm_index
            recognised.append(found)
    print(recognised)
    if found == testing_labels[sample_index]:
        total_found += 1
print("Total found: ", total_found)
