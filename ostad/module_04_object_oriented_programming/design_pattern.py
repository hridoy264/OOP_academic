# 1.  # singeleton design pattern

# class Singeleton:
#     _instance = None    # class variable

#     def __new__(cls):
#         if cls._instance is None:
#             print("1st object is created")
#             cls._instance = super(Singeleton, cls).__new__(cls)
#         return cls._instance

# ob1 = Singeleton()
# ob2 = Singeleton()

# print(ob1 is ob2)

# # 2. Factory Design Pattern

# class Car:
#     def driver(self):
#         return "Driving a car"
    
# class Bike:
#     def driver(self):
#         return "Riding a bike"
    
# class VehicleFactory:
#     @staticmethod
#     def get_vehicle(type):
#         if type == "car":
#             return Car()
#         elif type == "bike":
#             return Bike()
#         else:
#             return ValueError("Unknown bike")
        
# vehicle = VehicleFactory.get_vehicle("car")
# print(vehicle.driver())

# 3. Builder Design Pattern

class Computer:
    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def __str__(self):
        return f"Computer with {self.cpu} CPU, {self.ram} RAM, {self.storage} STORAGE"

class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
    def set_cpu (self, cpu):
        self.cpu = cpu
        return self
    def set_ram(self, ram):
        self.ram = ram 
        return self
    def set_storage(self, storage):
        self.storage = storage
        return self
    def build(self):
        return Computer(self.cpu, self.ram, self.storage)
    

builder = ComputerBuilder()
computer = builder.set_cpu("Intel i9").set_ram("32GB").set_storage("1TB SSD").build()
print(computer)