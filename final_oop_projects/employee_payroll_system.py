class Employee:
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    def calculate_pay(self):
        pass

    

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, department, hourly_rate, hours_work):
        super().__init__(name, employee_id, department)
        self.hourly_rate = hourly_rate
        self.hours_work = hours_work


    def calculate_pay(self):
        if self.hours_work >40:
            self.salary = 40 * self.hourly_rate + (self.hours_work - 40)*self.hourly_rate*1.5
        else:
            self.salary = self.hourly_rate * self.hours_work

    def display(self):
            print(f"Employee: {self.name} ID:{self.employee_id} - Pay: ${self.salary}")

class SalarriedEmployee(Employee):
    def __init__(self, name, employee_id, department, annual_salary):
            super().__init__(name, employee_id, department)
            self.annual_salary = annual_salary

    
    def calculate_pay(self):
        self.salary = self.annual_salary/12

    def display(self):
            print(f"Employee: {self.name} ID:{self.employee_id} - Pay: ${self.salary}")

e1 = HourlyEmployee("Shahnewaj Hriody", 264, "Robotics and Mechatronics Engineering", 234, 90)
e2 = SalarriedEmployee("ABC", 123, "asdlkfjiemf asdjfdasl ", 423423)

employees = [e1, e2]

def print_payroll(employees):
    for i in employees:
        i.calculate_pay()
        i.display()

print_payroll(employees)