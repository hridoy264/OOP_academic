class Student:
    def __init__(self, student_id, name, scores):
        self.__studentid = student_id
        self.__name = name
        self.__scores = scores

    def calculate_avg(self, list):
        sum = 0
        for i in list:
            sum += i
        avg = sum/len(list)
        return avg

    def get_scores(self):
        return self.__scores
    def get_id(self):
        return self.__id 
    def get_name(self):
        return self.__name
    

class STEMStudent(Student):
    def __init__(self, student_id, name, scores, lab):
        super().__init__(student_id, name, scores)
        self.class_work = self.calculate_avg(self.get_scores()) * 0.08
        self.lab_work = lab * 0.02

        self.total_mark = self.lab_work + self.class_work

    def display(self):
        print(f"ID: {self.get_id()}")
        print(f"Name: {self.get_name()}")
        print(f"Scores: {self.get_scores()}")
        print(f"Total avg marks: {self.total_mark}")

class ArtsStudent(Student):
    def __init__(self, student_id, name, scores, portfolio):
        super().__init__(student_id, name, scores)
        self.class_work = self.calculate_avg(self.get_scores()) * 0.07
        self.portfolio = portfolio * 0.03

        self.total_mark = self.portfolio + self.class_work


    def display(self):
        print(f"ID: {self.get_id()}")
        print(f"Name: {self.get_name()}")
        print(f"Scores: {self.get_scores()}")
        print(f"Total avg marks: {self.total_mark}")

st1 = STEMStudent(1, "Shahnewaj Hridoy", [90, 80, 99, 99, 95], 80)
st2 = ArtsStudent(2, "Sumaiya Shamsun Halim", [90, 87, 89, 99, 90], 98)

student_list = [st1, st2]

def generate_report_card(student_list):
    for i in student_list:
        i.display()

if __name__ == "__main__":
    generate_report_card(student_list)