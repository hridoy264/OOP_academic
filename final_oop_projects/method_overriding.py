class Vehicle:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    def move(self):
        print("Car is moving")

car1 = Car("Ford")
car1.move()