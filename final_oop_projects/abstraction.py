from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @property
    @abstractmethod
    def wheels(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

    @property
    def wheels(self):
        print("Car has 4 wheel")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")
    def stop(self):
        print("Bike is stopping")
    @property
    def wheels(self):
        print("Bike has only 2 wheels")

car = Car()
car.start()
car.stop()
car.wheels



