import os

from weka import Weka
from classifier import Classifier

if __name__ == "__main__":
    features = Weka(os.path.dirname(__file__) +
                    '/images').extractTo(fileName='caracteristicas')

    # retorno para o electron da extração das fetuares de todas as imagens da pasta images
    print(features)

    Classifier(data=features).NaiveBayes()
