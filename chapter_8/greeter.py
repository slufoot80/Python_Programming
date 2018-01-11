def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# This is an infinite loop!

while True:
    print("\nPlease tell me your name: ")
    f_name = raw_input("First name: ")
    if f_name == 'q':
        break

    l_name = raw_input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
