class Product:
    def __init__(self, name, price):
        self.name = name 
        self.price = price
    def what(self):
        print(f"It is {self.name}. Its price is only {self.price} bdt")
class ElectronicProduct(Product):
    def __init__(self, name, price, warrenty):
        super().__init__(name, price)
        self.warrenty = warrenty
    def what(self):
        print(f"It is {self.name}. Its price is only {self.price} bdt. It has warrenty for {self.warrenty}")

bulb = ElectronicProduct("Energy Bulb", 200, "1 years")
bulb.what()
