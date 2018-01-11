filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("Reading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents.title())
   # except FileNotFoundError:
        print(" Sorry, I can't find that file.")
