import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(self.x**2 + self.y**2)

    def plus(self, vector):
        print(self.x + vector.x, self.y + vector.y)
        return Vector(self.x + vector.x, self.y + vector.y)

    def minus(self, vector):
        print(self.x - vector.x, self.y - vector.y)
        return Vector(self.x - vector.x, self.y - vector.y)

    def __repr__():


vec = Vector(3, 4)
print(vec.length)
print(vec.plus(Vector(1, 2)))
