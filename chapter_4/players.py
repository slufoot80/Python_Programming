players = ['paula', 'frank','gabe','gena','sammy','lisa']
print("\nThis is the original list")
print(players)

print("\nThe list below is a sliced list for the first three names")
print(players[0:3])

print("\nThe list below prints the second third and fourth in the list")
print(players[1:4])

print("\nThe list below prints the the first four names in the list")
print(players[:4])

print("\nThe list below prints the last four players")
print(players[2:])

print("\nThe list below prints the last three players")
print(players[-3:])

print("\nThere are the first three players on my team")
for player in players[:3]:
  print(player.title())
