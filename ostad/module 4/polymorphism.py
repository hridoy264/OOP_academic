# poly -> multiple
# morphism -> form

# 1. Method overriding
class GrandFather:
    def __init__(self):
        self.__khajana = 30000      # private variable (Abstraction)
        self._age = 62      # protected
        self.name = 'hello'
    def greet(self):
        print("Grandfather says")

class Father(GrandFather):
    def greet(self):
        print(f"Father says {self._GrandFather__khajana}")
        print(self._age)
    
class Children(Father):
    def greet(self):
        print("Children says")

gf = GrandFather()
f = Father()
c = Children()

gf.greet()
f.greet()
c.greet()
# gf.__khajana()
# print(gf.name())



# 2. Method overloading

class Shape:
    # def area(a, b):
    #     return a*b
    # def area():
    #     return 10
    def area(self, a, b = 10):
        return a*b

p = Shape()
print(p.area(12))
print(p.area(5, 5))

