
from shapes import Rectangle, Circle

r = Rectangle()
r.display()
r.setWidth(1.25)
r.setHeight(1.25)
print("Get Width:", r.getWidth())
print("Get Height:", r.getHeight())
print("Area:", format(r.area(), ".5f"))

c = Circle(0)
c.display()
c.setRadius(10)
print("Get Radius:", c.getRadius())
print("Area:", format(c.area(), ".5f"))
print("Circumference:", format(c.circumference(), ".5f"))
