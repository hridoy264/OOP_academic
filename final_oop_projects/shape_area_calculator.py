from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length 
        self.width = width 
        self.area_type = "Rectangle"

    def area(self):
        area = self.length*self.width
        return area

    def __str__(self):
        return f"{self.area_type}: area = {self.area()}"
        

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 
        self.area_type = "Circle"

    def area(self):
        area = 3.14 * (self.radius)**2
        return area 

    def __str__(self):
            return f"{self.area_type}: area = {self.area()}"
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base 
        self.heigth = height
        self.area_type = "Triangle"

    def area(self):
        area = 0.5*self.base*self.heigth
        return area 

    def __str__(self):
            return f"{self.area_type}: area = {self.area()}"

        

rect = Rectangle(10, 20)
cir = Circle(13)
tri = Triangle(10, 12)

shpaes= [rect, cir, tri]

def print_areas(shapes):
    for i in shapes:
        print(i)


print_areas(shpaes)