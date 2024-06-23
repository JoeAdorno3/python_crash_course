#  program to check and see if usernames are already taken

current_users = ['JOHN', 'John123', 'TheLegend27', 'Chen_Zhao', 'Joe_Adorno_3']

new_users = ['John', 'TheLegend27', 'Odoamne', 'Primagen', 'Thorin Oakenshield']

lower_current_users = []

for user in current_users:
	lower_current_users.append(user.lower())

for user in new_users:
	if user.lower() in lower_current_users:
		print(f"The username '{user}' is unavailable, choose another username.")
	else:
		print(f"The username '{user}' is available.")
