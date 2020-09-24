# import pandas
import numpy as np
# import matplotlib.pyplot as plt

from time import time
from sklearn import model_selection, linear_model, preprocessing, metrics, naive_bayes
# from sklearn.metrics import plot_confusion_matrix
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

    scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
    rescaled_features = scaler.fit_transform(features)

    final_features = np.array(rescaled_features)
    final_labels = np.array(output)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(
      final_features, final_labels, test_size=0.35, train_size=0.65
    )

    self.__labels = np.unique(classes)

    return X_train, y_train, X_test, y_test

  # TODO: paramos aqui 
  def NaiveBayes():
    preprocessing
    Logger.log('')



    




