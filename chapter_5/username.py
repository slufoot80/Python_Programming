usernames = []

for username in usernames:
    if username == 'admin':
        print("Hello, "+ username.title() + ", would you like to see a status report?\n")
    else:
        print("Hello, " + username + ", Thank you for logging in again!\n")
else:
    print("We need to find some users")
