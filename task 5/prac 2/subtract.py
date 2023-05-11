class HeightDifference(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return str(self.feet) + " feet " + str(self.inches) + " inches"
    
    def __sub__(self, other):
        height_A_inches = self.feet *12 + self.inches
        height_B_inches = other.feet *12 + other.inches
        height_differecne_inches = height_A_inches - height_B_inches
        total_differnece_feet = height_differecne_inches // 12

        return  HeightDifference(total_differnece_feet, height_differecne_inches % 12)

person_height_A = HeightDifference(6, 4)
person_height_B = HeightDifference(4, 11)
height_disparity = person_height_A - person_height_B
print("heihgt difffernce is: ", height_disparity)