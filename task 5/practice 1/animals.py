class Animal():
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def __str__(self):
        output = "\nCLass: Animal\nName: " + \
            str(self.name) + "\nAge: " + str(self.age)
        return output

class HUman(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)

        self.set_name(name)


        self.friends = []

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def speak(self):
        print("hey shritz, how are you, i'm " + self.name)

    def __str__(self):
        output ="\nAge: " + str(self.age) +"\nFriends list: " 
        for friend in self.friends:
            output += friend + "\n "

        return output
    
a = Animal(5)
print(Animal)

human = HUman("mendel", 22)
human.add_friend("shritz")
human.add_friend("shlomo")
human.add_friend("yossi")
human.add_friend("yankel")
human.add_friend("yitzchok")
human.speak()
class Cat(Animal):
    def speak(self):
        print("Meow")

    def __str__(self):
        output = "\nClass: Cat\nName: " + \
            str(self.name) + "\nAge: " + str(self.age)
        return output


class Dog(Animal):
    def speak(self):
        print("Woof")

    def __str__(self):
        output = "\nClass: Dog\nName: " + \
            str(self.name) + "\nAge: " + str(self.age)
        return output


cat = Cat(3)
dog = Dog(5)

cat.set_name("dingass")
dog.set_name("sheritz")

print(cat, dog)
