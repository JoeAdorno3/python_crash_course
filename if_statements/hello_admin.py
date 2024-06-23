# program which goes through user names and greets each user depending on what their name is. if the name is "admin" then there's a special greeting"

usernames = ['TheLegend27', 'Megatron', 'admin', 'Chen_Zhao', 'Furry23']

for user in usernames:
	if user == 'admin':
		print(f"Hello, {user}, would you like to see a status report?")
	else:
		print(f"Hello {user}, thanks for logging in again.")


