import os

from weka import Weka
from classifier import Classifier

"""
    Init training for all images in a folder
"""
if __name__ == "__main__":
    features = Weka(os.path.dirname(__file__) +
                    './images').extractTo(fileName='caracteristicas')

    Classifier(data=features).NaiveBayes()
