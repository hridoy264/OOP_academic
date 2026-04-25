class Student:
    #class attribute
    school = "ABC High School"

    #instance attribute
    def __init__(self, name):
        self.name = name

s1 = Student("Rahim")
s2 = Student("Karim")

print(f"{s1.name} studies at {Student.school}")
print(f"{s2.name} studies at {Student.school}")
