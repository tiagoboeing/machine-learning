from weka import Weka
from classifier import Classifier

if __name__ == "__main__":
    features = Weka('../dataset/apu_nahasapeemapetilon').extractTo(fileName='caracteristicas')
    Classifier(data = features).NaiveBayes()
