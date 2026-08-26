class Parrot:
    #class attribute
    name = ""
    age=0

#create parrot1 object
Parrot1 = Parrot()
Parrot1.name = "kechi"
Parrot1.age = 5

#create another object Parrot2
Parrot2 = Parrot()
Parrot2.name = "pathor"
Parrot2.age = 3


#Access attributes
print(f"{Parrot1.name} is {Parrot1.age} years old")
print(f"{Parrot2.name} is {Parrot2.age} years old")

