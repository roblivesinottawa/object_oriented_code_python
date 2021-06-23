class Uber:

    # number_cars = 0
    number_passengers = 0

    def __init__(self, driver, kilometres, places, payment, passengers):
        self.driver = driver
        self.kilometres = kilometres
        self.places = places
        self.payment = payment
        self.passengers = passengers
        # Uber.number_cars  = Uber.number_cars + number_cars
        Uber.number_passengers = Uber.number_passengers + passengers

    def rate(self):
        return self.payment / self.kilometres

    @classmethod
    def number_cars(cls):
        return cls.number_cars

    @classmethod
    def average_num_passengers(cls):
        return int(cls.number_passengers / cls.number_cars)

    def __str__(self):
        return f"""The driver's name is {self.driver}. They have travelled {self.kilometres} kilometres on this run to {self.places}. 
        The cost of this trip was {self.payment} and there were {self.passengers} in the vehicle."""

car_one = Uber("John", 30, ["Ottawa", "Gatineau"], 70, 2)
print(car_one)