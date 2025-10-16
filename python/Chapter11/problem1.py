import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def add(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"


v2a = Vector2D(3, 4)
v2b = Vector2D(1, 2)
print("2D Vector Addition:", v2a.add(v2b))
print("2D Vector Magnitude:", v2a.magnitude())

v3a = Vector3D(2, 3, 6)
v3b = Vector3D(1, 1, 2)
print("\n3D Vector Addition:", v3a.add(v3b))
print("3D Vector Magnitude:", v3a.magnitude())
