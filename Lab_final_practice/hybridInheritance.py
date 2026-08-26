class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, university):
        self.name = name
        self.university = university
    def study(self):
        return f"I am studing at {self.university}"
class Employee(Person):
    def __init__(self, name, company):
        self.name = name
        self.company = company
    def work(self):
        return f"I am working at {self.company}"

class WorkingStudent(Student, Employee):
    def __init__(self, name, university, company):
        self.name = name 
        self.university = university
        self.company = company

hridoy = WorkingStudent("Shahnewaj Hridoy", "University of Dhaka", "Tesla")
print(hridoy.study())
print(hridoy.work())