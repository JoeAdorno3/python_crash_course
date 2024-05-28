# goal of list is to generate a list of cubes 

numbers = list(range(1,11))
cubes = []

for number in numbers: 
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)


# modifiying program to include slices for a list

print(f"the first three items in the list are {cubes[0:3]}")

print(f"three items from the middle of the list are are {cubes[3:6]}")

print(f"the last three items in the list are {cubes[-3:]}")

