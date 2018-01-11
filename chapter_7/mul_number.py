import os
os.system('clear')


number = int(raw_input("Give me a number, please: "))

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")

else:
    print(str(number) + " is not a multiple of 10.")

