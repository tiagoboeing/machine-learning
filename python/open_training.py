import os
import sys
import json

from weka import Weka
from classifier import Classifier

if __name__ == "__main__":

    features = Weka(os.path.dirname(__file__) +
                    '/images').extractTo(fileName='caracteristicas')

    Classifier(data=features).NaiveBayes()
