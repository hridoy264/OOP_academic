# class Student:
#     #class attribute
#     school = "ABC High School"

#     #instance attribute
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Rahim")
# s2 = Student("Karim")

# print(f"{s1.name} studies at {Student.school}")
# print(f"{s2.name} studies at {Student.school}")


class Student:
    school = "University of Dhaka"

    def __init__(self, name):
        self.name = name

student1 = Student("Shahnewaj")
student2 = Student("Arnob")
student3 = Student("Sakib")

print(f"{student1.name} studies at {Student.school}")
print(f"{student2.name} studies at {Student.school}")
print(f"{student3.name} studies at {Student.school}")