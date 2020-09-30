import base64
import io
import json
import os
import sys
import urllib
from itertools import chain

import h5py
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import model_selection, preprocessing, metrics, naive_bayes, tree

from read_image import ReadImage


class Classifier:
    def __init__(self, data=None):
        self.__labels = []
        self.__data = data
        self.__h5_data = os.path.dirname(__file__) + '/output/data.h5'
        self.__h5_labels = os.path.dirname(__file__) + '/output/labels.h5'

    def prepare(self):
        features, classes = [], []

        for image in self.__data:
            features.append(image[0:5])
            classes.append(image[6])

        self.__labels = np.unique(classes)
        preprocessed = preprocessing.LabelEncoder()
        output = preprocessed.fit_transform(classes)

        scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
        rescaled_features = scaler.fit_transform(features)

        final_features = np.array(rescaled_features)
        final_labels = np.array(output)

        h5f_data = h5py.File(self.__h5_data, 'w')
        h5f_data.create_dataset('dataset_1', data=final_features)

        h5f_label = h5py.File(self.__h5_labels, 'w')
        h5f_label.create_dataset('dataset_1', data=final_labels)

        h5f_data.close()
        h5f_label.close()

    def NaiveBayes(self):
        self.prepare()

        final_features, final_labels = self.load_dataset()

        X_train, X_test, y_train, y_test = model_selection.train_test_split(
            np.array(final_features), np.array(final_labels), test_size=0.35, train_size=0.65
        )

        model = naive_bayes.GaussianNB()
        model.fit(X_train, y_train)

        if sys.platform.startswith('linux'):
            self.confusion_matrix2(model, X_train, y_train)
        else:
            self.confusion_matrix(model, X_test, y_test)

    def DecisionTree(self):
        self.prepare()

        final_features, final_labels = self.load_dataset()

        X_train, X_test, y_train, y_test = model_selection.train_test_split(
            np.array(final_features), np.array(final_labels), test_size=0.35, train_size=0.65
        )

        model = tree.DecisionTreeClassifier()
        model.fit(X_train, y_train)

        if sys.platform.startswith('linux'):
            self.confusion_matrix2(model, X_train, y_train)
        else:
            self.confusion_matrix(model, X_test, y_test)

        # Tree
        print(tree.plot_tree(model))

    # https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py
    def confusion_matrix(self, model, x_test, y_test):
        title = "Matriz de confusão"

        disp = metrics.plot_confusion_matrix(
            model, x_test, y_test, cmap=plt.cm.Blues)

        disp.ax_.set_title(title)

        my_path = os.getcwd()
        filename = 'MatrizDeConfusao.png'
        file_path = my_path + '/public/' + filename

        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())

        confusion_matrix = {}

        confusion_matrix['uri'] = 'data:image/png;base64,' + \
                                  urllib.parse.quote(string)

        print(json.dumps(confusion_matrix))

    def confusion_matrix2(self, model, x_train, y_train):
        y_pred = model.predict(x_train)
        cf_matrix = metrics.confusion_matrix(y_train, y_pred)

        sns.heatmap(cf_matrix, annot=True)

        my_path = os.getcwd()
        filename = 'MatrizDeConfusao.png'
        file_path = my_path + '/public/' + filename

        fig = plt.gcf()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())

        confusion_matrix = {}

        confusion_matrix['uri'] = 'data:image/png;base64,' + \
                                  urllib.parse.quote(string)

        print(json.dumps(confusion_matrix))

    def load_dataset(self):
        h5f_data = h5py.File(self.__h5_data, 'r')
        h5f_label = h5py.File(self.__h5_labels, 'r')

        final_features_string = h5f_data['dataset_1']
        final_labels_string = h5f_label['dataset_1']

        final_features = np.array(final_features_string)
        final_labels = np.array(final_labels_string)

        h5f_data.close()
        h5f_label.close()

        return final_features, final_labels

    @staticmethod
    def predict(model, img, X_train, X_test, y_train, y_test):
        features_from_img = ReadImage().read(img=img)

        if model == 'naive-bayes':
            model = naive_bayes.GaussianNB()
        elif model == 'decision-tree':
            model = tree.DecisionTreeClassifier()

        model.fit(X_train, y_train)

        scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
        rescaled_feature = scaler.fit_transform(
            np.array(features_from_img[0:5]).reshape(-1, 1))

        predict = model.predict(X_test)
        prediction = model.predict(rescaled_feature.reshape(1, -1))[0]

        accuracy = metrics.accuracy_score(
            y_test, predict) * 100

        return prediction, features_from_img, accuracy

    def classify(self, img, model):
        final_features, final_labels = self.load_dataset()

        X_train, X_test, y_train, y_test = model_selection.train_test_split(
            final_features, final_labels, test_size=0.35, train_size=0.65
        )  # use 65% for training and 35% for tests

        prediction, features_from_img, accuracy = self.predict(model,
                                                               img, X_train, X_test, y_train, y_test)

        label = 'Apu'  # 0.0
        if prediction:
            label = 'Marge'  # 1.0

        # API send
        print(json.dumps({
            'features': {
                'Apu body': features_from_img[0],
                'Apu pants': features_from_img[1],
                'Apu shirt': features_from_img[2],
                'Marge body': features_from_img[3],
                'Marge hair': features_from_img[4],
                'Marge dress': features_from_img[5]
            },
            'prediction': {
                'accuracy': accuracy,
                'label': label
            }
        }))
