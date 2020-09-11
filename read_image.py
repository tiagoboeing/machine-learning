import os
import cv2
from logger import Logger
from range_color import Range


class ReadImage():
    def __init__(self):
        self.__width = 0
        self.__height = 0
        self.__bartOrangeShirt = 0
        self.__bartBlueShorts = 0
        self.__bartBlueShoe = 0
        self.__homerBluePants = 0
        self.__homerBrownMouth = 0
        self.__homerGreyShoe = 0
        self.__renderedImage = None
        self.__features = []
        self.__cloneImage = False

    def read(self, img, cloneImage=False):
        Logger.log(f'Image received {img}')
        image = cv2.imread(img)

        self.__cloneImage = cloneImage

        self.__height, self.__width, channels = image.shape

        if self.__cloneImage == True:
            Logger.log('Cloned image')
            self.__renderedImage = image.copy()

        Logger.log('Handle width and height')
        for height in range(self.__height):
            for width in range(self.__width):
                pixel = image[height, width]
                self.handleRangeColors(pixel, width, height)

        if self.__cloneImage == True:
            cv2.imshow('image', self.__renderedImage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return self.normalizeFeatures(img)

    """
      Receive a pixel (R, G, B) and call range_color.py
      https://stackoverflow.com/questions/28981417/how-do-i-access-the-pixels-of-an-image-using-opencv-python/50588950
    """

    def handleRangeColors(self, pixel, index_width, index_height):
        range = Range()
        b, g, r = pixel

        if range.isBartOrangeShirt(r, g, b):
            self.__bartOrangeShirt += 1

            if self.__cloneImage == True:
                self.set_color(self.__bartOrangeShirt,
                               index_width, index_height)

        if index_width > (self.__height / 2) and range.isBartBlueShorts(r, g, b):
            self.__bartBlueShorts += 1

            if self.__cloneImage == True:
                self.set_color(self.__bartBlueShorts,
                               index_width, index_height)

        if index_width > (self.__height / 2 + self.__height / 3) and range.isBartShoe(r, g, b):
            self.__bartBlueShoe += 1

            if self.__cloneImage == True:
                self.set_color(self.__bartBlueShoe, index_width, index_height)

        if range.isHomerBluePants(r, g, b):
            self.__homerBluePants += 1

            if self.__cloneImage == True:
                self.set_color(self.__homerBluePants,
                               index_width, index_height)

        if index_width < (self.__height / 2 + self.__height / 3) and range.isHomerMouth(r, g, b):
            self.__homerBrownMouth += 1

            if self.__cloneImage == True:
                self.set_color(self.__homerBrownMouth,
                               index_width, index_height)

        if index_width > (self.__height / 2 + self.__height / 3) and range.isHomerShoe(r, g, b):
            self.__homerGreyShoe += 1

            if self.__cloneImage == True:
                self.set_color(self.__homerGreyShoe, index_width, index_height)

    """
      TODO: estudar como associar uma variável recebida com o self
      Ex.: receber `variable` e associar self.variable += 1
    """

    def set_color(self, variable, index_width, index_height):
        self.__renderedImage[index_height][index_width] = [0, 255, 128]

    def calcNormalize(self, value):
        if(value != 0.0):
            return (value / (self.__width * self.__height)) * 100

        return 0.0

    """
      Normalizes the features by the number of total pixels of the image to % 
    """

    def normalizeFeatures(self, img):
        Logger.log('Normalize Features')

        self.__bartOrangeShirt = self.calcNormalize(self.__bartOrangeShirt)
        self.__bartBlueShorts = self.calcNormalize(self.__bartBlueShorts)
        self.__bartBlueShoe = self.calcNormalize(self.__bartBlueShoe)
        self.__homerBluePants = self.calcNormalize(self.__homerBluePants)
        self.__homerBrownMouth = self.calcNormalize(self.__homerBrownMouth)
        self.__homerGreyShoe = self.calcNormalize(self.__homerGreyShoe)

        bartOrHome = 0.0  # Bart
        filename = os.path.basename(img)[0]

        if filename == 'h':
            bartOrHome = 1.0  # Homer

        features = [
            self.__bartOrangeShirt,
            self.__bartBlueShorts,
            self.__bartBlueShoe,
            self.__homerBluePants,
            self.__homerBrownMouth,
            self.__homerGreyShoe,
            bartOrHome
        ]

        Logger.log(features)
        return features
