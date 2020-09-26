import os
import sys
import json

from weka import Weka
from classifier import Classifier
from read_image import ReadImage

if __name__ == "__main__":

    image = sys.argv[1]

    # Get uploaded image from args and read features
    features = {}
    features['features'] = ReadImage().read(img=image)
    print(json.dumps(features))

    features = Weka(os.path.dirname(__file__) +
                    '/images').extractTo(fileName='caracteristicas')

    Classifier(data=features).NaiveBayes()
