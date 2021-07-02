class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __str__(self):
        return f"The robot {self.name} was built in {self.build_year}"



x = Robot("Marvin", 1979)
y = Robot("Caliban", 1993)

print(x)
print(y)

