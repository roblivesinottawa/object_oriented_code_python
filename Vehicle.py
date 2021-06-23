class Vehicle:
    def __init__(self, model_year, max_speed, color, mileage, ):
        self.model_year = model_year
        self.max_speed = max_speed
        self.color = color
        self.mileage = mileage


    def accelerate(self):
        return f"this car can do as fast as {self.max_speed + 20} on the highway."


car = Vehicle(2016, 100, "black", 30000)
print(car.accelerate())
print(f"the color of the car is {car.color}, the current mileage is {car.mileage} and the year is {car.model_year}.")

