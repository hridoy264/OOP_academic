class Artist:
    def __init__(self, name):
        self.name = name    
    def draw(self):
        return "I can draw"

class Engineer:
    def __init__(self, field):
        self.field = field
    def build(self):
        return "I can build"

class Architect(Artist, Engineer):
    def __init__(self, name, field):
        Artist.__init__(self, name)
        Engineer.__init__(self, field)
        

archi = Architect("Shahnewaj Hridoy", "Robotics")
print(archi.draw())
print(archi.build())
