class Vehicle:

    minimum_rate = 50
    def __init__(self, model_year, max_speed, color, mileage):
        self.model_year = model_year
        self.max_speed = max_speed
        self.color = color
        self.mileage = mileage


    def accelerate(self):
        return f"this car can do as fast as {self.max_speed + 20} on the highway."

class Cab(Vehicle):
    minimum_rate = 75
    def __init__(self, model_year, max_speed, color, mileage, cab_type):
        super().__init__(self, model_year, max_speed, color, mileage)
        self.category = cab_type

class Bus(Vehicle):
    minimum_rate = 25
    def __init__(self, model_year, max_speed, color, mileage):
        super().__init__(self, model_year, max_speed, color)
        


car = Vehicle(2016, 100, "black", 30000)
print(car.accelerate())
print(f"the color of the car is {car.color}, the current mileage is {car.mileage} and the year is {car.model_year}.")

