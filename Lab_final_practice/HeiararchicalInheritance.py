class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        return "Vehicle is starting"

class Car(Vehicle):
    def start(self):
        return "Car is starting"

class Bike(Vehicle):
    def start(self):
        return "Bike is starting"

class Truck(Vehicle):
    def start(self):
        return "Truck is starting"

car = Car("Toyota")
bike = Bike("Honda")
truck = Truck("Nitaku")

print(car.start())
print(bike.start())
print(truck.start())
