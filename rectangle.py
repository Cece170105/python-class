'''2. Import Class 
a) Implement a class Rectangle with two attributes, width and height. 
b) Implement an init method with an optional parameter type. 
Set the default value of the attributes of width and height to 1. 
c) Implement a display method to print the values of width and height. 
d) Implement a setWidth method to assign width to the instance variable. 
e) Implement a setHeight method to assign height to the instance variable. 
f) Implement a getWidth method to return the value of the instance variable width. 
g) Implement a getHeight method to return the value of the instance variable height. 
h) Implement an area method to return the value of area of a rectangle. 
i) Save Rectangle class as rectangle.py. 
j) Import Rectangle class from rectangle.py.  
k) Employs the Rectangle class methods above to set and get various measurements of a rectangle.  
1) Instantiate two objects of type rectangle, one with arguments one without. 
r1 = Rectangle(4, 5) 
r2 = Rectangle() 
2) Call display() to print width and height. 
3) Call area() in print() to display the area of r1 and r2. 
4) Call setWidth() and setHeight() to update width and height to 6 of r2. 
5) Call getWidth() in print() to display the updated width of r2. 
6) Call getHeight() in print() to display the updated height of r2. 
7) Call area() in print() to display the area of r2. '''

# rectangle.py

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
    

    
