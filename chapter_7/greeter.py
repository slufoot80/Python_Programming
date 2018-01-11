prompt = "\nIf you tell us who you are, we can personalize the message you see." # original prompt variable
prompt += "\nWhat is your first name: " # appending prompt variable to the first variable

name = raw_input(prompt) # variable for input is set to name and I am passing the prompt variable to the input
print("\nHello, " + name + "!") # print function
