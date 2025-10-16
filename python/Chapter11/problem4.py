class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"



c1 = Complex(3, -2)
c2 = Complex(1, 7)

print("c1 =", c1)
print("c2 =", c2)

print("\nAddition:", c1 + c2)
print("Multiplication:", c1 * c2)
