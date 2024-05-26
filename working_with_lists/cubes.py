# goal of list is to generate a list of cubes 

numbers = list(range(1,11))
cubes = []

for number in numbers: 
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)
