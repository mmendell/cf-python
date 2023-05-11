class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __lt__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        return height_A_inches < height_B_inches

    def __gt__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        return height_A_inches > height_B_inches

    def __eq__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        return height_A_inches == height_B_inches

    def __le__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        return height_A_inches <= height_B_inches

    def __ge__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        return height_A_inches >= height_B_inches

    def __ne__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        return height_A_inches != height_B_inches


height1 = Height(4, 6)
height2 = Height(4, 5)
height3 = Height(5, 9)
height4 = Height(5, 10)

# print(height1 < height2)
print(height2 >= height2)
print(height3 == height4)
print(height1 != height3)
