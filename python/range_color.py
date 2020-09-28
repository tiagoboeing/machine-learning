class Range():
    """
    Extract characteristics from Apu Nahasapeemapetilon character
    """

    def apu_is_body(self, red, green, blue):
        return 100 <= red <= 200 and 30 <= green <= 130 and 0 <= blue <= 50

    def apu_is_pants(self, red, green, blue):
        return 189 <= red <= 220 and 175 <= green <= 210 and 119 <= blue <= 200

    def apu_is_shirt(self, red, green, blue):
        return 28 <= red <= 60 and 95 <= green <= 150 and 0 <= blue <= 35

    """
    Extract characteristics from Marge Simpson
    """

    def marge_is_body(self, red, green, blue):
        return 202 <= red <= 235 and 158 <= green <= 195 and 0 <= blue <= 50

    def marge_is_hair(self, red, green, blue):
        return 40 <= red <= 80 and 79 <= green <= 110 and 145 <= blue <= 255

    def marge_is_dress(self, red, green, blue):
        return 105 <= red <= 166 and 135 <= green <= 215 and 0 <= blue <= 123
