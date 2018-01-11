filename = 'programming_poll.txt'

responses = []
while True:
    response = raw_input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = raw_input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
