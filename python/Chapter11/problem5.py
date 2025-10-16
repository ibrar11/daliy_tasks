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

    def __len__(self):
        return len(self.components)

    def __str__(self):
        labels = ['i', 'j', 'k', 'l', 'm', 'n']
        parts = []

        for idx, val in enumerate(self.components):
            label = labels[idx] if idx < len(labels) else f"x{idx+1}"
            sign = '+' if val >= 0 else '-'
            formatted = f"{sign} {abs(val)}{label}"
            parts.append(formatted.strip())

        result = ' '.join(parts)
        if result.startswith('+'):
            result = result[2:]
        else: 
            result = '-' + result[2:] 

        return f"Vector({result})"
    

v1 = Vector([-12, 4, 6])
v2 = Vector([1, 3, 5])

print("v1 =", v1)
print("v2 =", v2)
print("\nAddition:", v1 + v2)
print("Dot Product:", v1 * v2)
print("Dimension of v1:", len(v1))
