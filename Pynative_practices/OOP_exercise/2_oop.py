class Vehicle:
    def __init__(self, name, max_speed, milaze):
        self.name = name
        self.max_speed = max_speed
        self.milaze = milaze

Vehicle1 = Vehicle("Toyota", 100, 23)
Vehicle2 = Vehicle("Marcidis", 150, 26)
Vehicle3 = Vehicle("Ferari", 200, 45)
print(f"Vehicle name: {Vehicle1.name}, Max speed: {Vehicle1.max_speed}, Milaze: {Vehicle1.milaze}")
print(f"Vehicle name: {Vehicle2.name}, Max speed: {Vehicle2.max_speed}, Milaze: {Vehicle2.milaze}")
print(f"Vehicle name: {Vehicle3.name}, Max speed: {Vehicle3.max_speed}, Milaze: {Vehicle3.milaze}")