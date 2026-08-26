class Person:
    def __init__(self, name):
        self.name = name 
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
    def introduce(self):
        print("My name is Omuk.")
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def teach(self):
        print("I love teaching.")
class Adminstrator(Person):
    def __init__(self, name):
        super().__init__(name)
    def manage(self):
        print("I love managing.")

p1 = Adminstrator("Shahnewaj Hridoy")
print(p1.name)
p1.manage()

p2 = Student("Anik")
print(p2.name)
p2.introduce()