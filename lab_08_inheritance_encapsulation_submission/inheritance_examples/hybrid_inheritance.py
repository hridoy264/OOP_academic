class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, university):
        self.name = name
        self.university = university
class Employee(Person):
    def __init__(self, name, company):
        self.name = name
        self.company = company
class WorkingStudent(Student, Employee):
    def __init__(self, name, university, company):
        Student.__init__(self, name, university)
        Employee.__init__(self, name, company)

hridoy=WorkingStudent("Shahnewaj Hriody", "University of Dhaka", "Tesla")
print(hridoy.name)
print(hridoy.university)
print(hridoy.company)