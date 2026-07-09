class Employee:
    company_name = "Ostad Academy"  # class variable
    def __init__(self, name, salary):
        self.name = name    # instance variable
        self._salary = salary   # instance variable

    @property       # Property decorator use korar somoy eta use korte hoy
    def salary(self):
        return self._salary
    
    @salary.setter      # to set a variable with property decorator
    def salary(self, new_salary):
        self._salary = new_salary

        
    
ob1 = Employee("Rahim", 40000)
print(ob1.salary)
ob1.salary = 70000
print(ob1._salary)