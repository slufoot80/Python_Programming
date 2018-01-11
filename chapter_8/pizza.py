def make_pizza(size, rosp, *toppings):

	"""Print a list of toppings that have been requested"""
        print("\nMaking a " + str(size) + " -inch " + str(rosp) + 
            " pizza with the following toppings:" ) 
        for topping in toppings:
            print("- " + topping.title())

#make_pizza(16, 'round','pepperoni',)
#make_pizza(24, 'square', 'mushrooms', 'green peppers', 'extra cheese')
