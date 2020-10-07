import sys
from classifier import Classifier

if __name__ == "__main__":

    image = sys.argv[1]
    model = 'naive-bayes'

    if len(sys.argv) > 2:
        model = sys.argv[2]

    # Predict image
    Classifier().classify(img=image, model=model)
