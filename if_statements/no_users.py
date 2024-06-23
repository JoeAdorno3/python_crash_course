# program which goes through user names and greets each user depending on what their name is. if the name is "admin" then there's a special greeting". If there are no users then a warning is printed

usernames = ['TheLegend27', 'Megatron', 'admin', 'Chen_Zhao', 'Furry23']

if usernames:
	for user in usernames:
		if user == 'admin':
			print(f"Hello {user}, would you like to see a status report?")
		else:
			print(f"Hello {user}, thanks for logging in again!")
else:
	print("We need to get some users!")


usernames = []



if usernames:
	for user in usernames:
		if user == 'admin':
			print(f"Hello {user}, would you like to see a status report?")
		else:
			print(f"Hello {user}, thanks for logging in again!")
else:
	print("We need to get some users!")



