class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animal is now making sound :)")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says Woof!")

dog = Dog("Tommy")
dog.make_sound()