# exercise 3.6 from chapter three of Python Crash Course, second edition. Builds off of the previous programs completed for exercises 3.4 and 3.5 (guest_list.py + changing_guest_list.py). 

# program begins by yanking previous program. In this case I've pulled over the entire changing_guest_list.py program

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

# beginning of exercise 3-6, wherein we begin by letting people know that we've found a bigger dinner table. 

print(f"\n\tGood news everyone! We've found a larger dinner table and now have room for three more guests. Please wait for your new invitations.")

# adding new guests at the bginning, middle, and end using the insert, insert, and append methods
guest_list.insert(0, 'Benjamin Franklin')
guest_list.insert(2, 'Otto VonBismark')
guest_list.append('Genghis Khan')

# printing a new set of invitations for everyone

print(f"\n\tDear {guest_list[0]}, you are cordially invited to dinner with {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, and {guest_list[5]}. Please RSVP with invites by 04/12/2024.")
print(f"\n\tDear {guest_list[1]}, you are cordially invited to dinner with {guest_list[0]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, and {guest_list[5]}. Please RSVP with invites by 04/12/2024.")
print(f"\n\tDear {guest_list[2]}, you are cordially invited to dinner with {guest_list[1]}, {guest_list[0]}, {guest_list[3]}, {guest_list[4]}, and {guest_list[5]}. Please RSVP with invites by 04/12/2024.")
print(f"\n\tDear {guest_list[3]}, you are cordially invited to dinner with {guest_list[1]}, {guest_list[2]}, {guest_list[0]}, {guest_list[4]}, and {guest_list[5]}. Please RSVP with invites by 04/12/2024.")
print(f"\n\tDear {guest_list[4]}, you are cordially invited to dinner with {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[0]}, and {guest_list[5]}. Please RSVP with invites by 04/12/2024.")
print(f"\n\tDear {guest_list[5]}, you are cordially invited to dinner with {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, and {guest_list[0]}. Please RSVP with invites by 04/12/2024.")

# modification to the program suggested at the end of the chapter, using the len() function to determine the length of the guest list

print(f"\nWe are going to hopefully have {len(guest_list)} guests coming over for dinner.")
