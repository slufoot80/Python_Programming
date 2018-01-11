import json

number = raw_input("What's your favorite number? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Thanks! I'll remember that.\n")

with open('favorite_number.json') as f:
    number = json.load(f)

print("I know your favorite number! It's " + str(number) + ".")
