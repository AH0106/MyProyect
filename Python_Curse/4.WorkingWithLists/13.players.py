
""" 
To make a slice, you specify the index of the first and last elements you want
to work with. As with the range() function, Python stops one item before the
second index you specify. To output the first three elements in a list, you
would request indices 0 through 3, which would return elements 0, 1, and 2.

"""

players = ['Charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])

print(players[1:4])

print(players[:4])# automatically starts your slice at the beginning of the list:

print(players[2:])

# if we want to output the last three players on the roster
print(players[-3:])


""" 
You can use a slice in a for loop if you want to loop through a subset of the 
elements in a list

"""

players = ['Charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team")

for player in players[:3]:
  print(player.title())