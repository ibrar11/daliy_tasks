class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        result = sum(a * b for a, b in zip(self.components, other.components))
        return result

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"
    

v1 = Vector([2, 4, 6])
v2 = Vector([1, 3, 5])

print("v1 =", v1)
print("v2 =", v2)
print("\nAddition:", v1 + v2)
print("Dot Product:", v1 * v2)
