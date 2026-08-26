class Car:
    def __init__(self, make, model, year):
        # Setting up attributes
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        # A method that uses the object's attributes
        print(f"The {self.year} {self.make} {self.model}'s engine is running!")

# Creating an object (an instance of the class)
my_car = Car("Toyota", "Camry", 2022)

# Calling the method
my_car.start_engine()