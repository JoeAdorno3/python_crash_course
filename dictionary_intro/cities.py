# purpose of program is to make a dictionary called cities; use the names of three cities as key's, and then include informatoin about each city such as country, population, and fact. After creating the dictionary w/ the cities I should print out all of the information that I have on each city. 

# creating cities in their dictionaries
cities = {
	'Holy Terra': {'Country': 'Imperium of Man', 
			'Population': 'Trillions of people', 
			'Fact': 'Capital planet for the Imperium of Man in the 40K setting, and current throne planet where the corpse emperor sits on his golden throne'}, 
	'Chicago': {'Country': 'United States of America', 
		'Population': '3 Million or so', 
		'Fact': 'Unofficial capital of the midwest, Chicago first grew to prominence during the 1800s as the gateway city which connected the East to the developing new west in America.'}, 
	'Beijing': {'Country': 'China', 
		'Population': '20 million (at a guess)',
		'Fact': 'Capital city of China, Beijing is home to many famous museums, tourist destinations, schools, etc. and is of critical importance to Chinese society.'},}

# printing out values from the dict
for city, city_info in cities.items():
	print(f"\nCity: {city}")
	print(f"City information following:\n Country: {city_info['Country']} \n Population: {city_info['Population']} \n Fact: {city_info['Fact']}")



