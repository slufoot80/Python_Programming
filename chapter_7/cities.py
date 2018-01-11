prompt = "\nPlease enter a name of a city you have not visited: "
prompt += "\nEnter 'quit' when you are finished: "

while True:
    city = raw_input(prompt)
    
    if city == 'quit':
        break
    else:
        print("\nI'd love to go to " + city.title() + "!!")
