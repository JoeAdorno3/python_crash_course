# create a list of numbers 1 --> 9 and then make sure to include the proper "th" or "st" ending for each in the output. each number should be on a new line

numbers = range(1,10)

for number in numbers:
	if number == 1:
		print(f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")


