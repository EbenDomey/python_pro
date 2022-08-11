class Circle():
    pi=3.14#u can call this by using self.pi or "ClassName"."attributeName" in this case Circle.pi
    def __init__(self, radius=2):
        self.radius=radius
    def circumference(self):
        return 2*self.pi*self.radius


myCircle = Circle(1)
print(myCircle.circumference())