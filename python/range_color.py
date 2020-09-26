class Range():

    """
    Extract characteristics from Apu Nahasapeemapetilon character
    """

    def apu_is_body(self, red, green, blue):
        if red >= 135 and red <= 157 and green >= 60 and green <= 70 and blue >= 0 and blue <= 35:
            return True
        return False

    def apu_is_pants(self, red, green, blue):
        if red >= 189 and red <= 220 and green >= 175 and green <= 206 and blue >= 119 and blue <= 151:
            return True
        return False

    def apu_is_shirt(self, red, green, blue):
        if red >= 32 and red <= 40 and green >= 101 and green <= 110 and blue >= 0 and blue <= 30:
            return True
        return False

    def merge_is_body(self, red, green, blue):
        if red >= 202 and red <= 235 and green >= 158 and green <= 181 and blue >= 8 and blue <= 14:
            return True
        return False

    def merge_is_hair(self, red, green, blue):
        if red >= 58 and red <= 71 and green >= 79 and green <= 102 and blue >= 152 and blue <= 255:
            return True
        return False

    def merge_is_dress(self, red, green, blue):
        if red >= 116 and red <= 166 and green >= 146 and green <= 191 and blue >= 76 and blue <= 123:
            return True
        return False
