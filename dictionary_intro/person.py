# create a basic dictionary to store information about a person

person = {'first_name': 'Barack', 'last_name': 'Obama', 'age': 62, 'city': 'Chicago'}
person1 = {'first_name': 'Chen', 'last_name': 'Zhao', 'age': 27, 'city': 'Chicago', }
person2 = {'first_name': 'Joe', 'last_name': 'Adorno', 'age': 27, 'city': 'Chicago'}

person_list = [person, person1, person2]

for person in person_list:
	print(f"The person's first name is: {person['first_name']}")
	print(f"The person's last name is: {person['last_name']}")
	print(f"The person's age is: {person['age']}")
	print(f"The person's city is: {person['city']}")

