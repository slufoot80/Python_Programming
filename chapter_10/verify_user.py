import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
#    except IOError:
    #except FileNotFoundError:
    except IOError:
        pass
        return None
    else:
        return username 

def get_new_username():
    """Prompt for a new username."""
    username = raw_input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

def greet_user():
    """Greet the user by usename."""
    username = get_stored_username()
    if username:
        correct = raw_input("Are you " + username + "? (y/n) ")
        if correct == 'y':
            print("Welcome back, " + username + "!")
            return

        username = get_new_username()
        print("We'll remember you when you come back, " +  username + "!")

greet_user()
