class Range():
    """
    Extract characteristics from Apu Nahasapeemapetilon character
    """

    def apu_is_body(self, red, green, blue):
        if 100 <= red <= 200 and 30 <= green <= 130 and 0 <= blue <= 50:
            return True
        return False

    def apu_is_pants(self, red, green, blue):
        if 189 <= red <= 220 and 175 <= green <= 210 and 119 <= blue <= 200:
            return True
        return False

    def apu_is_shirt(self, red, green, blue):
        if 28 <= red <= 60 and 95 <= green <= 150 and 0 <= blue <= 35:
            return True
        return False

    """
    Extract characteristics from Merge Simpsom
    """

    def merge_is_body(self, red, green, blue):
        if 202 <= red <= 235 and 158 <= green <= 195 and 0 <= blue <= 50:
            return True
        return False

    def merge_is_hair(self, red, green, blue):
        if 40 <= red <= 80 and 79 <= green <= 110 and 145 <= blue <= 255:
            return True
        return False

    def merge_is_dress(self, red, green, blue):
        if 166 >= red >= 116 <= green <= 215 and 50 <= blue <= 123:
            return True
        return False
