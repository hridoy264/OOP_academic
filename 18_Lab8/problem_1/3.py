class Organism:
    def __init__(self, name):
        self.name = name 
    def grow(self):
        print("I am growing")

class Plant(Organism):
    def photosynthesize(self):
        print("I can photosynthesis :)")

class FloweringPlant(Plant):
    def bloom(self):
        print("I have flowers and I can bloom them :3")

f_plant = FloweringPlant("Rose")
print(f_plant.name)
f_plant.grow()
f_plant.photosynthesize()
f_plant.bloom()
