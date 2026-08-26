class Vehicle:
    def __init__(self, name):
        self.name = name 
    def start(self):
        print("A vehicle is starting")
class Bike(Vehicle):
    def start(self):
        print("Bike is starting")
class Car(Vehicle):
    def start(self):
        print("Car is starting")
class Truck(Vehicle):
    def start(self):
        print("Truck is starting")

truck = Truck("Truck")
print(truck.name)
truck.start()
