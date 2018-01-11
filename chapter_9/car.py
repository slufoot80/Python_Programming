class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the cars mileage."""
        print("My " + my_new_car.get_descriptive_name() + " has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odomerter reading to a given  value."""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

my_new_car = Car('chevy', 'monte carlo', '1979')
print("My First Car was a: " + my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('chevy', 'monte carlo', '1979')
my_used_car.update_odometer(24)

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
