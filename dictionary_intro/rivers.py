# goal is to write a progrma which has a dictionary containing 'rivers': 'countries' and then work through some for loops with keys and values and f-strings


rivers = {
	'egypt': 'nile', 
	'iraq': 'tigris', 
	'brazil': 'amazon',
}


# loop which prints a sentence about each river

for k, v in rivers.items():
	print(f"The {v.title()} runs through the {k.title()}.")

print("\n")
# loop which prints the name of each river in the dictionary

for v in rivers.values():
	print(v.title())

print("\n")

# loop which prints the name of each country in the dictionary
for k in rivers.keys():
	print(k.title())
