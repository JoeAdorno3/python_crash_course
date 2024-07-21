# aliens example from the dictionary section, going to play around with some code and output here

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# making an empty list and appending aliens to it

print("Making a new list and appending aliens to it. should see 30 aliens added")

# making list
aliens = []

# making 30 aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# showing first five aliens
for alien in aliens[:5]:
	print(alien)
print("...")

# showing total aliens created
print(f"The total number of aliens is: {len(aliens)}")


print("\nAdjusting or modifiying three aliens")

# making list
aliens = []

# making 30 aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

# showing first five aliens
for alien in aliens[:5]:
	print(alien)
print("...")


