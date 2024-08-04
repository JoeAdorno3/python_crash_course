# goal of program is to come up with a list of favorite places for each person

favorite_places = {
	'chen': {'place_1': 'Taiyuan',
		'place_2': 'Beijing',
		'place_3': 'Chicago',},
	'joe': {'place_1': 'Boston',
		'place_2': 'Chicago',
		'place_3': 'Tariffville',},
	'biden': {'place_1': 'Scranton',
		'place_2': 'White House',
		'place_3': 'Deleware',},
}

# looping through dictionary and printing favorite places

for keys in favorite_places:
	print(f"\n{keys} favorite places are:" )
	for  value in favorite_places[keys].values():
		print(f"{value}")


 
