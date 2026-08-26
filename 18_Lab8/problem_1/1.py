class Animal:
    def __init__(self, name):
        self.name = name
    def sound():
        print("bark!")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        print(name)
    def sound(self):
        print("woof!")

dog = Dog("tommy")
dog.sound()