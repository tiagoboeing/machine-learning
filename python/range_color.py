class Range():

    """
    Extract characteristics from Apu Nahasapeemapetilon character
    """

    def apu_is_body(self, red, green, blue):
        if red >= 100 and red <= 200 and green >= 30 and green <= 130 and blue >= 0 and blue <= 50:
            return True
        return False

    def apu_is_pants(self, red, green, blue):
        if red >= 189 and red <= 220 and green >= 175 and green <= 210 and blue >= 119 and blue <= 200:
            return True
        return False

    def apu_is_shirt(self, red, green, blue):
        if red >= 28 and red <= 60 and green >= 95 and green <= 150 and blue >= 0 and blue <= 35:
            return True
        return False

    """
    Extract characteristics from Merge Simpsom
    """

    def merge_is_body(self, red, green, blue):
        if red >= 202 and red <= 235 and green >= 158 and green <= 195 and blue >= 0 and blue <= 50:
            return True
        return False

    def merge_is_hair(self, red, green, blue):
        if red >= 40 and red <= 80 and green >= 79 and green <= 110 and blue >= 145 and blue <= 255:
            return True
        return False

    def merge_is_dress(self, red, green, blue):
        if red >= 116 and red <= 166 and green >= 146 and green <= 215 and blue >= 50 and blue <= 123:
            return True
        return False
