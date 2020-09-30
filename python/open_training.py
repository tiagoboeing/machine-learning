import os
import sys
from datetime import datetime
from weka import Weka
from classifier import Classifier

"""
    Init training for all images in a folder
"""
if __name__ == "__main__":
    print("Started in", datetime.now().time())

    model = 'naive-bayes'
    if len(sys.argv) > 1:
        model = sys.argv[1]

    features = Weka(os.path.dirname(__file__) +
                    '/images').extractTo(fileName='caracteristicas')

    classifier = Classifier(data=features)

    if model == 'naive-bayes':
        classifier.NaiveBayes()
    elif model == 'decision-tree':
        classifier.DecisionTree()

    print("Ended time", datetime.now().time())
