import os
from datetime import datetime
from weka import Weka
from classifier import Classifier

"""
    Init training for all images in a folder
"""
if __name__ == "__main__":
    print("Started in", datetime.now().time())

    features = Weka(os.path.dirname(__file__) +
                    '/images').extractTo(fileName='caracteristicas')

    Classifier(data=features).NaiveBayes()

    print("Ended time", datetime.now().time())