class Artist:
    def __init__(self, name):
        self.name = name
    def draw(self):
        print("I can draw")
class Engineer:
    def __init__(self, field):
        self.field = field
    def build(self):
        print("I can build")

class Architect(Artist, Engineer):
    def __init__(self, name, field):
        Artist.__init__(self, name)
        Engineer.__init__(self, field)


architect = Architect("Hridoy", "Robotics")

print(architect.name)
print(architect.field)
architect.draw()
architect.build()