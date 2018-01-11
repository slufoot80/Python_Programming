def greet_users(names):						# defining function and initializing varaible name
    """Print a simple greeting to each user in the list"""
    for name in names:    					# for loop
        msg = "Hello, " + name.title() + "!"                    # setting variable to message and name variable
        print(msg)                                              # printing variable

usernames = ['frank', 'gabe', 'gena'] 				# setting list to variable name

greet_users(usernames)					        # calling function name
