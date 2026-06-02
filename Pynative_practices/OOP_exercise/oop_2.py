class Vehicle:
    def __init__(self, name, max_speed, milaze):
        self.name = name
        self.max_speed = max_speed
        self.milaze = milaze

Vehicle1 = Vehicle("Toyota", 100, 23)
print(f"Vehicle name: {Vehicle1.name}, Max speed: {Vehicle1.max_speed}, Milaze: {Vehicle1.milaze}")