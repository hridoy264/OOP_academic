class Student:
    def __init__(self, student_id, name, scores):
        self.__studentid = student_id
        self.__name = name
        self.__scores = []
        self.set_scores(scores)
    def set_scores(self, score_list):
        for i in score_list:
            if type(i) != int:
                raise TypeError("Scores must be integers")
            if i<0 or i>100:
                raise ValueError("Scores must be between 0 and 100")
        self.__scores = score_list

    def calculate_avg(self):
        return sum(self.__scores)/len(self.__scores)

    def get_scores(self):
        return self.__scores
    def get_id(self):
        return self.__studentid 
    def get_name(self):
        return self.__name
    

class STEMStudent(Student):
    def __init__(self, student_id, name, scores, lab):
        super().__init__(student_id, name, scores)
        self.lab_work = lab 

    def calculate_avg(self):
        return super().calculate_avg()*0.8 + self.lab_work*0.2


    def display(self):
        print(f"ID: {self.get_id()}")
        print(f"Name: {self.get_name()}")
        print(f"Scores: {self.get_scores()}")
        print(f"Total avg marks: {self.calculate_avg()}")

class ArtsStudent(Student):
    def __init__(self, student_id, name, scores, portfolio):
        super().__init__(student_id, name, scores)
        self.portfolio = portfolio 
    def calculate_avg(self):
        return super().calculate_avg()*0.7 + self.portfolio* 0.3



    def display(self):
        print(f"ID: {self.get_id()}")
        print(f"Name: {self.get_name()}")
        print(f"Scores: {self.get_scores()}")
        print(f"Total avg marks: {self.calculate_avg()}")


def generate_report_card(student_list):
    for i in student_list:
        i.display()
        print()
try:
    st1 = STEMStudent(1, "Shahnewaj Hridoy", [90, 80, 99, 99, -95], 80)
    st2 = ArtsStudent(2, "Sumaiya Shamsun Halim", [90, 87, 89, 99, 90], 98)

    student_list = [st1, st2]
    generate_report_card(student_list)

except ValueError as e:
    print(e)

except TypeError as e:
    print(e)

