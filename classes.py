class black_box:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.light_status = "Off"
    def light_status(self, status):
        self.light_status = status
            
class super_box(black_box):
    def __init__(self, name, color, explode_force):
        super().__init__(name, color)
        self.explode_force = explode_force
        
        

box1 = black_box("funkybox", "red")
box2 = black_box("coolbox", "blue")
superbox = super_box("super_duper_box", "black", 22)
print(superbox.name)
print(superbox.color)
print(superbox.explode_force)
