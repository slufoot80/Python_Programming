# Original Pizza list
favorite_pizza = ['Build your Own','BBQ Chicken Pizza','BBQ Chicken','Chicken Bacon Ranch','Buffalo Chicken Pizza','Buffalo Chicken','Asian Chicken Pizza','Asian Chicken','Specialty Pizza delivery','Howie Special','Works Pizza','Works','Howie Maui Pizza','Howie Maui','Meat Eaters Pizza delivery','Meat Eaters','Veggie Pizza','Veggie','Bacon Cheddar Cheeseburger Pizza','Bacon Cheddar Cheeseburger',]

# My Favorite Pizza List
my_pizza = (favorite_pizza[1:4])
print("\nMy favorite pizza's are: " + str(my_pizza))

# Gena's Favorite List
gena_pizza = my_pizza[:]
print("\nGena's favorite pizza's are: " + str(gena_pizza))

gena_pizza.append(favorite_pizza[-1:])
print("Gena also likes " + str(gena_pizza))
