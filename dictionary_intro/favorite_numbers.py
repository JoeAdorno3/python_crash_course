# using a dictionary to store people's favorite numbers

favorite_numbers = {
	'Joe': [42, 22, 45], 
	'Jim C': [23, 99, 69],
	'Barack': [44, 99, 100],
	'Gabe Newell': [3, 5, 7, 9],
	'Aliens Franchise': [2],
}
# printing out peoples favorite numbers

for  k,v in favorite_numbers.items():
	print(f"\n{k}'s favorite numbers are:")
	if len(v) > 1:
		for i in v:
			print(f"{i}")
	else:
		print(f"{v[0]}")


