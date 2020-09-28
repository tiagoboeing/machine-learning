import os
import cv2

from range_color import Range
from logger import Logger


class ReadImage():
    def __init__(self):
        self.__width = 0
        self.__height = 0
        self.__renderedImage = None
        self.__features = []
        self.__displayImage = False

        self.__apuBody = 0
        self.__apuPants = 0
        self.__apuShirt = 0
        self.__margeBody = 0
        self.__margeHair = 0
        self.__margeDress = 0

    def read(self, img, displayImage=False):
        Logger.log(f'Image received {img}')
        image = cv2.imread(img)

        self.__displayImage = displayImage

        self.__height, self.__width, channels = image.shape

        if self.__displayImage == True:
            Logger.log('Cloned image')
            self.__renderedImage = image.copy()

        Logger.log('Handle width and height')
        for height in range(self.__height):
            for width in range(self.__width):
                pixel = image[height, width]
                self.handleRangeColors(pixel, width, height)

        if self.__displayImage == True:
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

        # check for Apu characteristics
        if range.apu_is_body(r, g, b):
            self.__apuBody += 1
            if self.__displayImage == True:
                self.set_color(self.__apuBody, index_width, index_height)

        if range.apu_is_pants(r, g, b):
            self.__apuPants += 1
            if self.__displayImage == True:
                self.set_color(self.__apuPants, index_width, index_height)

        if range.apu_is_shirt(r, g, b):
            self.__apuShirt += 1
            if self.__displayImage == True:
                self.set_color(self.__apuShirt, index_width, index_height)

        # check for marge
        if range.marge_is_body(r, g, b):
            self.__margeBody += 1
            if self.__displayImage == True:
                self.set_color(self.__margeBody, index_width, index_height)

        if range.marge_is_hair(r, g, b):
            self.__margeHair += 1
            if self.__displayImage == True:
                self.set_color(self.__margeHair, index_width, index_height)

        if range.marge_is_dress(r, g, b):
            self.__margeDress += 1
            if self.__displayImage == True:
                self.set_color(self.__margeDress, index_width, index_height)

    """
      TODO: estudar como associar uma variável recebida com o self
      Ex.: receber `variable` e associar self.variable += 1
    """

    @classmethod
    def set_color(self, variable, index_width, index_height):
        self.__renderedImage[index_height][index_width] = [0, 255, 128]

    def calcNormalize(self, value):
        if (value != 0.0):
            return (value / (self.__width * self.__height)) * 100

        return 0.0

    """
      Normalizes the features by the number of total pixels of the image to % 
    """

    def normalizeFeatures(self, img):
        Logger.log('Normalize Features')

        self.__apuBody = self.calcNormalize(self.__apuBody)
        self.__apuPants = self.calcNormalize(self.__apuPants)
        self.__apuShirt = self.calcNormalize(self.__apuShirt)
        self.__margeBody = self.calcNormalize(self.__margeBody)
        self.__margeHair = self.calcNormalize(self.__margeHair)
        self.__margeDress = self.calcNormalize(self.__margeDress)

        apuOrmarge = 0.0  # Apu
        filename = os.path.basename(img)[0]

        if filename == 'm':
            apuOrmarge = 1.0  # marge

        features = [
            self.__apuBody,
            self.__apuPants,
            self.__apuShirt,
            self.__margeBody,
            self.__margeHair,
            self.__margeDress,
            apuOrmarge
        ]

        Logger.log(features)
        return features
