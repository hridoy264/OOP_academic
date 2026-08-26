class Light:
    def __init__(self):
        pass
    def turn_on(self):
        self.stat = "ON"
        print("Light is ON")
    def turn_off(self):
        self.stat = "OFF"
        print("Light is OFF")
    def status(self):
        print(f"Current status {self.stat}")


light = Light()
light.turn_on()
light.status()
light.turn_off()
light.status()
