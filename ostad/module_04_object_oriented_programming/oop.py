# Car class banabo, setar object banabo
# Brand, model


# __init__() : Dunder(duble underscore) method, constructor
# Constructor 3 types
# 1. Default Constructor
# 2. Parameterized constructor
# 3. Default Value Constructor

# amra normally jake function boli, seta ke class er moddhe banale amra take method boli

class Car:
    def __init__(self):     # self ei car class er object ke indicate kore
        self.brand = ""
        self.model = ""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 

    def __init__(self, brand = "Honda", model= "Civic"):
        self.brand = brand
        self.model = model

    def display_info(self):     # Instance Method
        print(f"Car Brand: {self.brand}\nCar Model: {self.model}")

car1 = Car("Toyota", "Corolla")
# car1.brand = "Toyota"
# car1.model = "corolla"
print(car1.brand)
print(car1.model)

car2 = Car()
# car2.brand = "Honda"
# car2.model = "Civic"
print(car2.brand)
print(car2.model)

car1.display_info()
car2.display_info()