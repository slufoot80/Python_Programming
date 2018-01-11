usernames = ['eric','willie','admin','erin','ever']

for username in usernames:
    if username == 'admin':
        print("Hello, "+ username.title() + ", would you like to see a status report?\n")
    else:
        print("Hello, " + username + ", Thank you for logging in again!\n")
