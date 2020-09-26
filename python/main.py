from weka import Weka
from classifier import Classifier

if __name__ == "__main__":
    features = Weka('./images').extractTo(fileName='caracteristicas')
    Classifier(data = features).NaiveBayes()
