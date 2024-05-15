# for the final exercise, 3-7, I need to take the program that I wrote for 3-6 and then use the pop() method to remove guests from the guest list until only two remain, send a message to each one after they've been popped, and then eventually send invites to the two remaining folks on teh guest list. Afterwards, I need to use del to remove the final two names and then print out the guest_list so it's confirmed that they've been deleted. 

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

# beginning work on program 3-7 here

print("\n\tHello dinner party attendees! Unfortunately, that spiffy new table that I'd ordered still hasn't arrived and we only have room for two guests at our prestigious dinner party. Please stand by for new invites or confirmation that we don't have room for you at the party.") 

# popping guests off of the list and printing a new message for them here.
popped_guest = guest_list.pop()
print(f"\n\tDear {popped_guest}, it is with a heavy heart that I must disinvite you from our dinner party. Please keep a weather eye out for new invitations so that we might catch up in the future.")
 
popped_guest = guest_list.pop()
print(f"\n\tDear {popped_guest}, it is with a heavy heart that I must disinvite you from our dinner party. Please keep a weather eye out for new invitations so that we might catch up in the future.")
 
popped_guest = guest_list.pop()
print(f"\n\tDear {popped_guest}, it is with a heavy heart that I must disinvite you from our dinner party. Please keep a weather eye out for new invitations so that we might catch up in the future.")
 
popped_guest = guest_list.pop()
print(f"\n\tDear {popped_guest}, it is with a heavy heart that I must disinvite you from our dinner party. Please keep a weather eye out for new invitations so that we might catch up in the future.")

# printing new invitations here

print(f"\n\t Dear {guest_list[0]}, please know that you are still cordially invited to dinner alongside {guest_list[1]}. I hope that you can still make it.")

print(f"\n\t Dear {guest_list[1]}, please know that you are still cordially invited to dinner alongside {guest_list[0]}. I hope that you can still make it.")

# deleting remaining guests off using the delete function
del guest_list[0]
del guest_list[0]

# printing guest_list to confirm that it has no people on it
print(guest_list)

