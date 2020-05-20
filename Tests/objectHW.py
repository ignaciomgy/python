import math

class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

l = Line((2,3), (8,10))
print(l.distance())
print(l.slope())



class Cylinder():
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
    
    def volume(self):
        return (self.height* math.pi * (self.radius**2))

    def surface_area(self):
        return 2*math.pi*self.radius

        