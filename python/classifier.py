import os
import numpy as np
import matplotlib.pyplot as plt

from time import time
from sklearn import model_selection, linear_model, preprocessing, metrics, naive_bayes
from logger import Logger


class Classifier:
    def __init__(self, data):
        self.__labels = []
        self.__data = data

    def prepare(self):
        features, classes = [], []

        for image in self.__data:
            features.append(image[0:5])
            classes.append(image[6])

        preprocessed = preprocessing.LabelEncoder()
        output = preprocessed.fit_transform(classes)

        scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
        rescaled_features = scaler.fit_transform(features)

        final_features = np.array(rescaled_features)
        final_labels = np.array(output)

        X_train, X_test, y_train, y_test = model_selection.train_test_split(
            final_features, final_labels, test_size=0.35, train_size=0.65
        )

        self.__labels = np.unique(classes)

        return X_train, y_train, X_test, y_test

    # TODO: falta score, e classicar uma imagem única
    def NaiveBayes(self):
        X_train, y_train, X_test, y_test = self.prepare()

        model = naive_bayes.GaussianNB()
        model.fit(X_train, y_train)

        self.confusion_matrix(model, X_test, y_test)

    # https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py
    def confusion_matrix(self, model, X_test, y_test):
        title = "Matriz Confusão"

        disp = metrics.plot_confusion_matrix(model, X_test, y_test)

        disp.ax_.set_title(title)

        my_path = os.path.dirname(__file__)
        plt.savefig(my_path + '/MatrizDeConfusão.png')
        print(True)
