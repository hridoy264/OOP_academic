# class Dog:
#     #class attribute
#     attr1 = "mammal"

#     #Instance attribute
#     def __init__(self, name):
#         self.name = name 

# #Driver code
# #Object instantiation
# Rodger = Dog("Rodger")
# Tommy = Dog("Tommy")

# #Accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attr1))
# print("Tommy is also a {}".format(Tommy.__class__.attr1))


# #Accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))


class Dog:
    #class attribute
    species = "mammal"

    #instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def speak(self):
        print("Ghew Ghew")

    def eat(self):
        print("I am busy to eat")
    
Dog1 = Dog("Tommy", 4)

Dog1.speak()
print(f"{Dog1.name} is {Dog1.age} years old and It is a {Dog.species}")
Dog1.eat()
