class Vehicle:
    def __init__(self, make, model, year):
        self.make = make 
        self. model = model 
        self. year = year 

    def display(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year,num_doors, engine_capacity):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.engine_capacity = engine_capacity

    def display(self):
            print(f"Make: {self.make}")
            print(f"Model: {self.model}")
            print(f"Year: {self.year}")
            print(f"Number of Doors: {self.num_doors}")

    def fuel_efficiency(self, engine_capacity):
         self.fuel_efficiency = 100/(0.5*engine_capacity)

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, sidecar, engine_capacity):
          super().__init__(make, model, year)
          self.sidecar = sidecar
          self.engine_capacity = engine_capacity

    def fuel_efficiency(self):
        self.fuel_efficiency = 100/(0.8*self.engine_capacity)

    def display(self):
                print(f"Make: {self.make}")
                print(f"Model: {self.model}")
                print(f"Year: {self.year}")
                print(f"Sidecar: {self.sidecar}")


car1 = Car("Tokyo", "ABC", 2023, 4, 50)
car2 = Car("Roles royece", "DEF", 2024, 4, 100)
mot1 = Motorcycle("SDF", "sdf", 2026, True, 23)
mot2 = Motorcycle("SDFe", "lkj", 2342, False, 45)



vehicles = [car1, car2, mot1, mot2]

def display_info(vehicles):
     for i in vehicles:
          i.display()
          print()

display_info(vehicles)