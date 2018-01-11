import os
os.system('clear')

height = float(raw_input("How tall are you in inches? "))

if height >= 36:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou will be able to ride when you are a little older.")
