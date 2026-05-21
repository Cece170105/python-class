"""3. Import Class 
a) Import pi only from math module. 
b) Implement a class Circle with an attribute, radius. 
c) Implement an init method with an optional parameter type. 
Set the default value of the attributes of radius to 1. 
d) Implement a display method to print the value of radius. 
e) Implement a setRadius method to assign radius to the instance variable. 
f) Implement a getRadius method to return the value of the instance variable radius. 
g) Implement an area method to return the value of area of a circle. 
h) Implement a circumference method to return the value of circumference of a circle. 
i) Save Rectangle class and Circle class as shapes.py. 
Page 2 of 2 
j) Import Rectangle class and Circle class from shapes.py.  
k) Employs the Rectangle class methods and Circle class methods above and set and get various measurements of a     
rectangle and a circle. """

from math import pi

class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def display(self):
        print("Width:", self.width)
        print("Height:", self.height)

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def display(self):
        print("Radius:", self.radius)

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def area(self):
        return pi * (self.radius ** 2)

    def circumference(self):
        return 2 * pi * self.radius
