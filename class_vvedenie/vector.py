import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x**2 + self.y**2)**0.5

    def angle(self):
        radians = math.atan2(self.y, self.x)
        return math.degrees(radians)

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y
vector1 = Vector(3,4)
vector2 = Vector(1,2)
vector3 = vector1.add(vector2)
vector4 = vector1.subtract(vector2)
scalar = vector1.dot(vector2)
print(vector3.x, vector3.y)
print(vector4.x, vector4.y)
print(scalar)