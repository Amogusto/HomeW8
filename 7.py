class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'y = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'y = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'y = {self.a} + {self.b} * i'


y1 = ComplexNumber(5, 6)
y2 = ComplexNumber(-1, 2)
print(y1)
print(y2)
print(y1 + y2)
print(y1 * y2)