# initial guest list for a dinner party w/ three guests
guest_list = ['Barack Obama', 'Julius Caesar', 'Leonardo DaVinci']

# invitation messages to each of them
print(f"\n\tDear {guest_list[0]}, you are cordially invited to dinner with {guest_list[1]} and {guest_list[2]}. Please RSVP by 04/05/2024.")

print(f"\n\tDear {guest_list[1]}, you are cordially invited to dinner with {guest_list[0]} and {guest_list[2]}. Please RSVP by 04/05/2024.")

print(f"\n\tDear {guest_list[2]}, you are cordially invited to dinner with {guest_list[1]} and {guest_list[0]}. Please RSVP by 04/05/2024.")

# writing a message to notify people that one of the guests can't make it

print(f"\n\tUh-oh, it looks like {guest_list.pop(1)} was just stabbed by his enemies (and Brutus). We'll work on finding a new guest for our fantastic dinner party.")


# adding Wu Zetian to the guest_list

guest_list.append('Wu Zetian')

#sending out new invitations

print(f"\n\tDear {guest_list[0]}, you are cordially invited to dinner with {guest_list[1]} and {guest_list[2]}. Please RSVP by 04/05/2024.")

print(f"\n\tDear {guest_list[1]}, you are cordially invited to dinner with {guest_list[0]} and {guest_list[2]}. Please RSVP by 04/05/2024.")

print(f"\n\tDear {guest_list[2]}, you are cordially invited to dinner with {guest_list[1]} and {guest_list[0]}. Please RSVP by 04/05/2024.")

