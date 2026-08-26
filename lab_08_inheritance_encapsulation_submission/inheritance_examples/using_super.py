class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price 
class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

light = ElectronicProduct("Torch Light", 264, '2 years')
print(light.name)
print(light.price)
print(light.warranty)


        