class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Vector: {self.a, self.b}"

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


vector_one = Vector(2, 10)
vector_two = Vector(5, -10)
print(vector_one + vector_two)