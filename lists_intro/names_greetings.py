# list of names
names = ['Chen Zhao', 'Colin Churchill', 'Julie Adorno', 'Mike Kokines']
# printing out each name manually
print(names[0])
print(names[1])
print(names[2])
print(names[-1])

# working on writing a message to each person using their name; going to use fstrings on them

message = f'I love my wife, {names[0]}, more than anyone else in the world'
print(message)

message = f'{names[1]} is my best friend from middle school and high school'
print(message)

message = f"{names[2]} is my mom, she's the best"
print(message)

message = f'{names[-1]} was a great friend from high school, we were both on the track team'
print(message)
