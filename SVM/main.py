import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay, classification_report
from SVM import SVM
import mnist
import argparse
from constants import LEARNING_SIZE, TESTING_SIZE, LAMBDA_DEFAULT, EPOCHS_DEFAULT, LEARNING_RATE_DEFAULT

czumpi_array = mnist.test_images()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-lamb",
                        help="Lambda parameter for minimising (lambda * ||w||^2)",
                        default=LAMBDA_DEFAULT)
    parser.add_argument("-lr",
                        help="Learning rate",
                        default=LEARNING_RATE_DEFAULT)
    parser.add_argument("-e",
                        help="Number of epochs in training",
                        default=EPOCHS_DEFAULT)
    args = parser.parse_args()
    lambda_param = float(args.lamb)
    learning_rate = float(args.lr)
    epochs = int(args.e)

    svms = []
    for i in range(10):
        # if i != 5:
        svms.append(SVM(lambda_param, i))
    # else:
    #     svms.append(SVM(0.01, i))

    print("Training for mnist dataset:")
    training_set, training_labels = mnist.train_images()[:LEARNING_SIZE], mnist.train_labels()[:LEARNING_SIZE]
    training_set = training_set.reshape(training_set.shape[0], -1) / 255.0

    testing_set = mnist.test_images()[:TESTING_SIZE]
    testing_set = testing_set.reshape(testing_set.shape[0], -1) / 255.0
    testing_labels = mnist.test_labels()[:TESTING_SIZE]

    for svm in svms:
        # if svm.target_number == 5:
        #     svm.train(training_set, training_labels, 0.1, epochs)
        # else:
        svm.train(training_set, training_labels, learning_rate, epochs)

    total_found = 0
    y_predicted = []
    for sample_index in range(testing_set.shape[0]):
        found = -1
        recognised = []
        for svm_index in range(10):
            result = svms[svm_index].predict(testing_set[sample_index])
            if result == 1 and svm_index == testing_labels[sample_index]:
                found = svm_index
                recognised.append(found)
        y_predicted.append(found)
        if found == testing_labels[sample_index]:
            total_found += 1
    labels = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Accuracy score: ", accuracy_score(testing_labels, y_predicted))
    print("General report: ", classification_report(testing_labels, y_predicted))
    cm = confusion_matrix(testing_labels, y_predicted, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot()
    plt.show()


if __name__ == "__main__":
    main()
