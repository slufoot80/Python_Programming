class Restaurant(object):
    """A class representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """display a message that the restaurant is open."""
        msg = self.name + " is open Come on in!" 
        print("\n" + msg)

    def set_number_served(self, number_served):
        """All user to set the number of customers that have been served."""
        self.number_served = number_served

class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""
    
    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize and ice cream stand."""
        super(IceCreamStand,self).__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()
