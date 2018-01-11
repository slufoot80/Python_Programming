favorite_toppings = ['pizza sauce', 'premium mozzarella', 'pepperoni', 'ham', 'hamburger', 'Italian sausage', 'bacon', 'mushrooms', 'onions', 'green peppers', 'black olives']
print("\nThis is the original pizza topping list is: \n" + str(favorite_toppings))

p = favorite_toppings[:3]
print("\nThis is the first 3 toppings in the list are: ")
print(p)

p = favorite_toppings[3:8]
print("\nThis list prints some of the middle toppings: ")
print(p)

p = favorite_toppings[-3:]
print("\nThis list prints the last three toppings: ")
print(p)
