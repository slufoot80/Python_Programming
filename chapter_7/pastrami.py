sandwich_orders = [ 'pastrami', 'veggie', 'grilled cheese', 'pastrami', 'turkey', 'roast beef', 'pastrami']
finished_sandwichs = []
sandwich_orders.sort()
print("Current available sandwiches are: " + str(sandwich_orders))

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("Current sandwich orders available: " + str(sandwich_orders))
