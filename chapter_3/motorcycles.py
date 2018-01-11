motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []                            # Start with empty list
print(motorcycles)                          # Print empty list

motorcycles.append('ducati')                # Append new item to empty list
print(motorcycles)

motorcycles.append('yamaha')
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)                          # Print new list

motorcycles.insert(0, 'honda')
print(motorcycles)

del motorcycles[1]                          # delete motorcycles in postition 1
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print("Popped motorcycles is " + popped_motorcycles.title())

motorcycles = ['honda', 'yamaha', 'suzuki', 'harley davison']
print(motorcycles)

owned = motorcycles[0]
print("\nThe first motorcycle I owned was a " + owned)

owned = motorcycles[1]
print("\nThe second motorcycle I owned was a " + owned)

owned = motorcycles[2]
print("\nThe third motorcycle I owned was a " + owned)

owned = motorcycles[3]
print("\nThe fourth motorcycle I owned was a " + owned)
