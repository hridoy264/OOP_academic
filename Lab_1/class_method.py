class Dog:
    #class attribute
    species = "mammal"

    #instance attribute
    def __init__(self, name):
        self.name = name

    #creating a method
    def speak(self):
        print("My name is {}".format(self.name))

Jodu = Dog("Jodu")
Modu = Dog("Modu")

Jodu.speak()
Modu.speak()