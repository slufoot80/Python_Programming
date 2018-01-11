# Start with users that need to be verified
# and an empty list to hold confirmed users.

unconfirmed_users = [ 'alice', 'brian', 'candance']
confirmed_users = []

# Verify each user until there are not more unconfirmed users.
# Move each verified user into the list of confirmed users.

print(" ")
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title()) 
