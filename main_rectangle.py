

from rectangle import Rectangle

r1 = Rectangle(4, 5)
r2 = Rectangle()

r1.display()
print("Area:", r1.area())

r2.display()
print("Area:", r2.area())

r2.setWidth(6)
r2.setHeight(6)

print("Get Width:", r2.getWidth())
print("Get Height:", r2.getHeight())
print("Area:", r2.area())
