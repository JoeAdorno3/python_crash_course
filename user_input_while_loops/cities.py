# basic program which works by taking in user input on a city that you've visted + send a basic message afterwards

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True: 
	city = input(prompt)
	
	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")


