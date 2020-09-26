class Range():

    def isBartOrangeShirt(self, red, green, blue):
        if 7 <= blue <= 90 and 70 <= green <= 105 and 200 <= red <= 255:
            return True
        return False

    def isBartBlueShorts(self, red, green, blue):
        if 170 >= blue >= 125 >= green >= 5 and 0 <= red <= 20:
            return True

        return False

    def isBartShoe(self, red, green, blue):
        if 125 <= blue <= 140 and 3 <= green <= 12 and 5 <= red <= 20:
            return True

        return False

    def isHomerBluePants(self, red, green, blue):
        if blue >= 150 and blue <= 180 and green >= 98 and green <= 120 and red >= 0 and red <= 90:
            return True

        return False

    def isHomerMouth(self, red, green, blue):
        if 140 >= blue >= 95 <= green <= 185 and 175 <= red <= 200:
            return True

        return False

    def isHomerShoe(self, red, green, blue):
        if 45 >= blue >= 25 <= green <= 45 and 25 <= red <= 45:
            return True

        return False
