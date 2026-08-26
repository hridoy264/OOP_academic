class Employee:
    def __init__(self, name, employee_id, basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.basic_salary = basic_salary
        self.total_salary = basic_salary

    def calculate_salary(self):
        print(f"Basic_salary: {self.basic_salary} ")

    def display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Basic_salary: {self.basic_salary} ")
        print(f"Total Salary: {self.total_salary}")
        print()
    
    

class Managers(Employee):
    def __init__(self, name, employee_id, basic_salary, fixed_bonus):
        super().__init__(name, employee_id, basic_salary)
        self.fixed_bonus = fixed_bonus
        self.total_salary = self.calculate_salary()

    def calculate_salary(self):
        total_salary = self.basic_salary + self.fixed_bonus
        return total_salary

class Developers(Employee):
    def __init__(self, name, employee_id, basic_salary, payment_per_hour, overtime_hour):
        super().__init__(name, employee_id, basic_salary)
        self.payment_per_hour = payment_per_hour
        self.overtime_hour = overtime_hour
        self.total_salary = self.calculate_salary()


    def calculate_salary(self):
        total_salary = self.basic_salary + self.payment_per_hour*self.overtime_hour
        return total_salary

class Researchers(Employee):
    def __init__(self, name, employee_id, basic_salary, research_allowance, no_of_published_paper):
        super().__init__(name, employee_id, basic_salary)
        self.research_allowance = research_allowance
        self.no_of_published_paper = no_of_published_paper
        self.total_salary = self.calculate_salary()

    def calculate_salary(self):
        total_salary = self.basic_salary + self.research_allowance*self.no_of_published_paper
        return total_salary

emp1 = Employee("Nabil Rahman", 123131, -20000)
emp2 = Researchers("Samsung Galaxy", 1212, 90, 9, 10)
emp3 = Developers("Shahnewaj Hridoy", 264, 9999999, 90, 26)
emp4 = Managers("JAS", 1, -10000, -0)




employee_list=[emp1, emp2, emp3, emp4]

def display_info(employee_list):
        for i in employee_list:
            i.display()

display_info(employee_list)