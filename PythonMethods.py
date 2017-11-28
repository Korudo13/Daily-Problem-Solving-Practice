# Create a method that returns the perimeter of a Circle class. 

class Circle(object):

    # class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def get_perimeter(self):
        return (2 * Circle.pi) * self.radius

c = Circle(radius=10)
print c.get_perimeter()
