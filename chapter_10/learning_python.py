filename = 'learning_python.txt'

print("___Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents.title())


print("___Looping over the lines:____")
with open(filename) as f: 
    for line in f:
      print(line.rstrip().title())

print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip().title())

print("\n--- Replace the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    """Get rid of a new line, ten replace Python with C."""
    line = line.rstrip()
    print(line.replace('python', 'c').title())
