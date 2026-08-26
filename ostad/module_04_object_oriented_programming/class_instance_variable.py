class School:
    school_name = "Ostad High School" # Class variable

    def __init__(self, name):
        self.student_name = name        # instance variable

sc1 = School("Rahim")
sc1.school_name = "Quantum Cosmo School"
School.school_name = "Class variable changed school"
print(sc1.school_name)
print(sc1.student_name)

sc2 = School("Karim")
print(sc2.school_name, sc2.student_name)