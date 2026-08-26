# Association

# Student, Laptop

class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_v = laptop_obj
    
    def show_laptop_info(self):
        print(f"{self.name} has a laptop named {self.laptop_v.brand}")

lp1 = Laptop("Asus")
student = Student("Rahim", lp1)
student.show_laptop_info()


# Aggregation : has a relationship (weak relationship)

# A university has departments 

class Department: 
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []
    def add_department(self, department):
        self.departments.append(department)

    def show_departments(self):
        return [department.name for department in self.departments]
    
un1 = University("ABC")
dep1 = Department("Programming")
dep2 = Department("Math")
un1.add_department(dep1)
un1.add_department(dep2)
print(un1.show_departments())


# Composition (strong relationship)
# Car, engine

class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)

    def show_details(self):
        print(f"{self.brand} has an engine with {self.engine.power} HP")


car = Car("Toyota", 100)
car.show_details()