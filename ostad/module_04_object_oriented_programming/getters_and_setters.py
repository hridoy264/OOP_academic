class Employee:
    company_name = "Ostad Academy"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary       # by convention, _variable name eta dhora hoy private variable, but logically private hoy na

    def get_salary(self, password):
        if password == "admin":
            print(self._salary)
        else:
            print("Invalid Accesss!!")
    
    def set_salary(self, password, salary):
        if password == 'admin':
            self._salary = salary
            print(f"New Salary: {self._salary}")
        else:
            print("Invalid Access!!!")


ob1 = Employee("Rahim", 30000)
ob2 = Employee("Karim", 50000)

ob1.get_salary('admin')
ob1.set_salary('admin', 70000)
# ob1._salary = 60000
print(ob1._salary)