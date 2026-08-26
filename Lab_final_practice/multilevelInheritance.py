class Organism:
    def __init__(self, name):
        self.name = name
    def grow(self):
        return "I am growing :)"

class Plant(Organism):
    def photosynthesize(self):
        return "I can photosynthesis :3"

class FloweringPlant(Plant):
    def bloom(self):
        return "I have flowers and I can bloom them :>"

rose = FloweringPlant("Rose")
print(rose.grow())
print(rose.photosynthesize())
print(rose.bloom())