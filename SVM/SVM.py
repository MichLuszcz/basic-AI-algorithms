import numpy as np


class SVM:

    def __init__(self, lambda_param, target_number):
        self.bias = 0
        self.weights = None
        self.lambda_param = lambda_param
        # the number the machine is trying to recognise
        self.target_number = target_number

    def train(self, x: np.ndarray, y: np.ndarray, learning_rate=0.01, epochs=1000):
        # The number of Samples in X
        number_of_samples = x.shape[0]

        # The number of features in X
        number_of_features = x.shape[1]
        self.weights = np.zeros(number_of_features)
        binary_labels = np.where(y == self.target_number, 1, -1)

        for _ in range(epochs):
            for sample_index in range(number_of_samples):
                # our cost function for single specimen = lambda * ||w||^2 + max(0, 1 - yi * (w * xi - b))
                # this means that its just lambda * ||w||^2 when yi * f(x) >= 1

                derivative_condition = binary_labels[sample_index] * (
                        np.dot(x[sample_index], self.weights) - self.bias) >= 1

                if derivative_condition:
                    self.weights -= learning_rate * (2 * self.lambda_param * self.weights)
                else:
                    self.weights -= (learning_rate *
                                     (2 * self.lambda_param * self.weights
                                      - np.dot(x[sample_index], binary_labels[sample_index])))
                    self.bias = learning_rate * binary_labels[sample_index]

        return self.weights, self.bias

    def predict(self, x):
        return np.sign(np.dot(x, self.weights) - self.bias)
