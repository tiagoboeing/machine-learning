import os
import sys

from weka import Weka
from classifier import Classifier
from read_image import ReadImage

if __name__ == "__main__":

    image = sys.argv[1]

    # print(ReadImage().read(img=image))

    features = Weka(os.path.dirname(__file__) +
                    '/images').extractTo(fileName='caracteristicas')

    # retorno para o electron da extração das fetuares de todas as imagens da pasta images
    print(features)

    Classifier(data=features).NaiveBayes()
