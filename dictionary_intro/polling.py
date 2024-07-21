# making a list of people and "polling" them about their favorite langauges. Depending on the results they'll get a different response

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

# making list of people who should take the poll 

people = ['jen', 'sarah', 'joe', 'mike']

for person in people:
	print(f"Hi {person.title()}.")
	if person in favorite_languages.keys():
		print(f"Thanks {person.title()} for taking the poll!")
	else:
		print(f"{person.title()}, please take our poll about favorite programming languages!")

