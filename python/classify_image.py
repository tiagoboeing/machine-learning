import os
import sys
import json

from weka import Weka
from classifier import Classifier
from read_image import ReadImage

if __name__ == "__main__":

    image = sys.argv[1]
    model = sys.argv[2]

    # Predict image
    Classifier().classify(img=image, model=model)
