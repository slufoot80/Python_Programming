numbers = range(1,21)
print(numbers)

numbers = range(2,1000001,2)
print(numbers)

numbers = list(range(1, 10000001))

print("The minimum number is: " + str(min(numbers)))
print("The maximum number is: " + str(max(numbers)))
print("The sum of all numbers is: " + str(sum(numbers)))

print("Printing odd numbers from 1 to 5000")
numbers = range(1,5001,2)
print(numbers)

print("\nPrinting multiples of 3, from number 3 to number 30")
numbers = range(3,31,3)
print(numbers)

print("\nBelow is a multi line ordinary list")
cubes = []
for value in range(1,11):
  cube = value**3
  cubes.append(cube)
print(cubes)

print("\nBelow is a single line comprension list")
cubes = [value**3 for value in range(1,11)]
print(cubes)
