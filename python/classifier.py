import os
import io
import json
import numpy as np
import matplotlib.pyplot as plt
import urllib
import base64
import h5py

from time import time
from sklearn import model_selection, linear_model, preprocessing, metrics, naive_bayes
from logger import Logger
from read_image import ReadImage


class Classifier:
    def __init__(self, data=None):
        self.__labels = []
        self.__data = data
        self.__h5_data = os.path.dirname(__file__) + './output/data.h5'
        self.__h5_labels = os.path.dirname(__file__) + './output/labels.h5'

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

        self.confusion_matrix(model, X_test, y_test)

    # https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py
    def confusion_matrix(self, model, X_test, y_test):
        title = "Matriz Confusão"

        disp = metrics.plot_confusion_matrix(model, X_test, y_test)

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

    def classify(self, img):
        final_features, final_labels = self.load_dataset()

        X_train, X_test, y_train, y_test = model_selection.train_test_split(
            np.array(final_features), np.array(final_labels), test_size=0.35, train_size=0.65
        )

        # Inicializa modelo
        model = naive_bayes.GaussianNB()

        # TODO: Treinar Modelo

        # Extrai caracteristicas e label da imagem
        featuresFromImg = {}
        featuresFromImg['features'] = ReadImage().read(img=img)
        print(json.dumps(featuresFromImg))

        # TODO: extrair apenas as features da variavel features para realizar o predict
        # TODO: Fazer predict e retornar o label correspondente a imagem. Ex: 0 - Bart; 1 - Homer
