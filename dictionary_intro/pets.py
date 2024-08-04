# goal of program is to make several dictionaries to represent pets, then put htem in a list, iterate through the list, and then push them through to print everything about them


julius = {
	'name': 'Julius',
	'animal': 'cat', 
	'age': 4, 
	'owner': 'Chen Zhao', 
	'favorite_activities': 'stealing food',
}

lulu = {
	'name': 'Lulu',
	'animal': 'cat', 
	'age': 4, 
	'owner': 'Chen Zhao', 
	'favorite_activities': 'being cute',
}

pet_list = [julius, lulu]

for pet in pet_list:
	print(f"\nThis pet is {pet['name']}")
	print(f"These are their pet facts.")
	for category, information in pet.items():
		print(f"{category}: {information}")
