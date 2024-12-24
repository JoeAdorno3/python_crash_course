# goal of program is to make a "parrot" program which captures user input and then spits it back to them; fairly straightforward

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active: 
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)


