class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.lower()
        self.email = email.lower()
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information"""
        print("\n" + self.first_name + " " + self.last_name)
        print(" Username: " + self.username)
        print(" Email:    " + self.email)
        print(" Location: " + self.location)

    def greet_user(self):
        """display a personalized greeting to the user."""
        print("\nWelcome Back, " + self.first_name + ' ' + self.last_name + "!")

    def increment_login_attempts(self):
        """Increment the value of login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset Login attpemtps to 0."""
        self.login_attempts = 0

eric = User('eric', 'matthes', 'ematthes', 'ematthes@programming.com', 'california')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...""")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("    Login attempts: " + str(eric.login_attempts))
print("\nResetting login attempts...")
eric.reset_login_attempts()
print("   Login attempts: " + str(eric.login_attempts))

willie = User('willie', 'burger', 'willieburger', 'wb@programming.com', 'michigan')
willie.describe_user()
willie.greet_user()

print("\nMaking 3 login attempts...""")
willie.increment_login_attempts()
willie.increment_login_attempts()
willie.increment_login_attempts()
print("    Login attempts: " + str(willie.login_attempts))

print("\nResetting login attempts...")
willie.reset_login_attempts()
print("   Login attempts: " + str(willie.login_attempts))
