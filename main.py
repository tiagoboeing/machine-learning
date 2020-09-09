import os
import cv2
from log import Logger

class Main():
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

    def readImage(self, img):
      Logger.log('Image received {img}') 
      image = cv2.imread(img)

      Logger.log('Image copyed')
      self.__renderedImage = image.copy()      
      self.__height, self.__width, channels = image.shape

      Logger.log('Handle width and height')
      for width in range(self.__width):
        for height in range(self.__height):
          pixel = image[height, width]
          self.handleRangeColors(pixel)                
          self.normalize(img)   
          print(f'Width: {width} - Height: {height} - Pixel: {pixel}')

      cv2.imshow('image', image)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

    """
        Receive a pixel (R, G, B) and call range_color.py
    """
    def handleRangeColors(self, pixel):
        range = Range()
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        
        if(range.isBartOrangeShirt(r, g, b)):
          self.__bartOrangeShirt++
          self.__renderedImage.put(i, j, new double[]{0, 255, 128});
        
        if(i > (h/2) && range.isBartBlueShorts(r, g, b)):
          self.__bartBlueShorts++
          self.__renderedImage.put(i, j, new double[]{0, 255, 128});
        
        if (i > (h/2 + h/3) && range.isBartShoe(r, g, b)):
          self.__bartBlueShoe++;
          self.__renderedImage.put(i, j, new double[]{0, 255, 128});
        
        if(range.isHomerBluePants(r, g, b)):
          self.__homerBluePants++;
          self.__renderedImage.put(i, j, new double[]{0, 255, 255});
        
        if(i < (h/2 + h/3) && range.isHomerMouth(r, g, b)):
          self.__homerBrownMouth++;
          self.__renderedImage.put(i, j, new double[]{0, 255, 255});
        
        if (i > (h/2 + h/3) && range.isHomerShoe(r, g, b)):
          self.__homerGreyShoe++;
          self.__renderedImage.put(i, j, new double[]{0, 255, 255});

    """
      Normalizes the features by the number of total pixels of the image to % 
    """
    def normalizeFeatures(self):      
      Logger.log('Normalize Features')      
      
      self.__bartOrangeShirt = (self.__bartOrangeShirt / (self.__width * self.__height)) * 100;
      self.__bartBlueShorts = (self.__bartBlueShorts / (self.__width * self.__height)) * 100;
      self.__bartBlueShoe = (self.__bartBlueShoe / (self.__width * self.__height)) * 100;
      self.__homerBluePants = (self.__homerBluePants / (self.__width * self.__height)) * 100;
      self.__homerBrownMouth = (self.__homerBrownMouth / (self.__width * self.__height)) * 100;
      self.__homerGreyShoe = (self.__homerGreyShoe / (self.__width * self.__height)) * 100;

      print(os.path.basename())

      features = [
        self.__bartOrangeShirt, 
        self.__bartBlueShorts, 
        self.__bartBlueShoe, 
        self.__homerBluePants, 
        self.__homerBrownMouth,
        self.__homerGreyShoe,
        filename = os.path.basename("path/to/file/sample.txt")
      ]


if __name__ == "__main__":
    Main().readImage('test.jpg')