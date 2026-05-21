'''1. Class Implementation 
a) Implement a class Rectangle with two attributes, width and height. 
b) Implement an init method with an optional parameter type. 
Set the default value of the attributes of width and height to 1. 
c) Implement a display method to print the values of width and height. 
d) Instantiate two objects of type rectangle, one with arguments one without. 
r1 = Rectangle(4, 5) 
r2 = Rectangle() 
e) Call display() to print width and height. 
f) Access and print the attribute values of r1 and r2.'''

class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def display(self):
        print("Width:", self.width)
        print("Height:", self.height)


r1 = Rectangle(4, 5)
r2 = Rectangle()

r1.display()
r2.display()

print("Width of r1 and r2:")
print(r1.width, "&", r2.width)

print("Height of r1 and r2:")
print(r1.height, "&", r2.height)
