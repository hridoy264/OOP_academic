# # 1. Single Inheritance

# # 2. Multilevel inheritance
# class GrandFather:
#     def __init__(self, color, first_name):
#         self.color = color
#         self.first_name = first_name

#     def gf_method(self):
#         print("I am from Grandfather")

# class Father(GrandFather):
#     def __init__(self, hobby, color, first_name):
#         super().__init__(color, first_name)
#         self.hobby = hobby

#     def father_method(self):
#         print("I am from Father")

# class Children(Father, GrandFather):
#     def __init__(self, fashion, hobby, color, first_name):
#         super().__init__(hobby, color, first_name)
#         self.fashion = fashion



# gf1 = GrandFather("Red", "Chowdhury")
# f1 = Father('Cricket', 'Red', 'Chowdhury')
# print(f1.hobby)
# print(f1.first_name)
# c1 = Children("Test", "Badminton", "Red", "Chowdhury")
# c1.gf_method()
# c1.father_method()
# print(c1.fashion)
# print(c1.fashion, c1.color, c1.first_name)


# #   3. Multilevel inheritance

# 4. Hierarchical

# class Vehicle:
#     def engine_type(self):
#         print("Vehicle has an engine")

# class Car(Vehicle):
#     def num_doors(self):
#         print("Car has 4 doors")
        
# class Truck(Vehicle):
#     def load_capacity(self):
#         print("Truck can carry 10 tons")

# car = Car()
# car.engine_type()
# car.num_doors()
# truck = Truck()
# truck.engine_type()
# truck.load_capacity()

class Shape:
    def area(self):
        print("Calculating area ...")

class Polygon(Shape):
    def sides(self):
        print("Polygon has multiple sides.")

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
rec = Rectangle(10, 5)
rec.sides()
print(rec.area())


# Inheritance ta aro valo kore bojha lagbe




