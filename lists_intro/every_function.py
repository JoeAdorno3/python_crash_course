# goal of this program is to use every single function listed in the chapter for lists at least once. I think that the best way to do this would be to make two lists, one listing all of the functions in the chapter at least once, and another which adds them after they've been used.We'll see how this goes....

# functions that I can find are:
# using the index[] function of the list in order to retreive specific functions
# using the .title() function in conjunction with the index function to make sure things are properly capitalized
# indexing at -1 in order to return the last item of a list
# using individual list values in an F-string
# using index values in order to change the specific value of one of the list items
# using the .append() function in order to add avlues to the end of a list
	# reccomended to use the # append() function to build lists dynamically; ie start with an empty list and then work on adding values as people work through the list
# using the insert() function in order to insert list values anywhere in teh list by specifying the index element and then specifiying the value
# using del in order to delete values in a particular location from the list
# using the .pop() function in order to remove a value from the end of a list and then use that function once it's been removed
# using the .pop() function to remove a value from any part of the list
# usign the .remove() function in order to remove list values that match up with the value that you listed
	# wonder if you can use the remove function to remove multiple values at once
# using the .sort() method in order to re-arrange things alphabetically
# using .sort() method where reverse=True in order to sort the list by reverse alphabetical order
# using the sorted() fuction in order to print a temprorarily sorted list
# using the sorted() function where reverse=True in order to print out  a sorted version of the list
# using the .reverse() function on the list in order to reverse it
# using the len() function to find the exact length/number of entries in the list 

#defining functions that I need to use as throughout the chapter
function_list = ['index[]', '.title()', 'index[-1]', '.append()', 'insert()', 'del', '.pop()', '.pop(_)', '.remove()', '.sort()', 'sort(reverse=True)', 'sorted()', 'sorted(a, reverse=True)', '.reverse()', 'len()']

# keeping track of functions that I still have remaining
remaining_functions = function_list 

# keeping track of functions that I have used
used_functions = []

# printing out lists at the start to see if they're good to go
print(f"This is the original list of functions which were used in Chapter 3\n {function_list}")
print(f"\nThis is the copied list of functions which I'll be using to keep track of how many functions I have left\n {remaining_functions}")
print(f"\nThis is the list of functions which I've used at this point in the exercise\n{used_functions}")

# list of food items that I want to make and include on my blog eventually
chinese_recipes = ['dan dan mian', 'mala tang', 'homemade hot pot broth', 'rou jia mou', 'liang pi', 'biang biang noodles', 'cumin lamb', 'chinese carbonara(fusion)', 'mao cai', 'hong shao yv', 'soy sauce noodles', 'scallion pancakes', 'sourdough mantou', 'baozi', 'jiaozi', 'noodle sauce recipe', 'dumpling sauce recipe']
print(f"\nThis is a list of chinese recipes which I want to include on my blog\n{chinese_recipes}")

# index function check and removal + addition check
print(f"\nIndex function check:\n{chinese_recipes[0]}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# title() with indexing check
print(f"\nTitle with indexing:\n{chinese_recipes[0].title()}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# last position using index[-1]
print(f"\nThis is the last item on the list\n{chinese_recipes[-1]}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# append function
chinese_recipes.append('error')
chinese_recipes.append('hong shao pai gu')
print(f"\nAppended Chinese Recipe list\n{chinese_recipes}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# insert check
chinese_recipes.insert(0, 'beef and potato stew')
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# del function check
del chinese_recipes[chinese_recipes.index("error")]
print(f"\nThis is the recipe list without the error added\n{chinese_recipes}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# creating a new chinese recipe list which I can remove from without damaging the original
chinese_recipes_copy = chinese_recipes
blogged_recipes = []
blogged_recipes.append(chinese_recipes_copy.pop())

# pop check
print(f"\nI've made these recipes from the list and put them on my blog\n{blogged_recipes}")
print(f"\nChecking to see if the pop() worked\n{chinese_recipes_copy}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# pop(_) check
blogged_recipes.append(chinese_recipes_copy.pop(5))
print(f"\nI've made these recipes from the list and put them on my blog\n{blogged_recipes}")
print(f"\nChecking to see if the pop() worked\n{chinese_recipes_copy}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# remove() function check
chinese_recipes_copy.remove('chinese carbonara(fusion)')
print(f"\nRemoving the chinese carbonara recipe from the copied list\n{chinese_recipes_copy}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# .sort() check
blogged_recipes.sort()
print(f"\nSorted list for blogged recipes\n{blogged_recipes}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# .sort(reverse=True) check
blogged_recipes.sort(reverse=True)
print(f"\nReverse sorted list for blogged recipes\n{blogged_recipes}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# testing out the sorted() function in a print statement 
print(f"\nCheck out this Sorted version of the original recipe list using the sorted() function\n{sorted(chinese_recipes)}")
print(f"\nOriginal list for proof that it's not sorted:\n{chinese_recipes}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# testing out the sorted(reverse=True) function in a print statement 
print(f"\nCheck out this Reverse  Sorted version of the original recipe list using the sorted() function\n{sorted(chinese_recipes, reverse=True)}")
print(f"\nOriginal list for proof that it's not sorted:\n{chinese_recipes}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")

# reverse function check
chinese_recipes_copy.reverse()
print(f"\nCheck out this Reversed version of the Copy of the original Chinese Recipe list  using the .reverse() function\n{chinese_recipes_copy}")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")


# len function check
print(f"\nThe original chinese recipe list contains {len(chinese_recipes)} items.")
used_functions.append(remaining_functions.pop(0))

# function check
print(f"\nThis is the copied list of functions which I have left in the program\n {function_list}")
print(f"\nThis is the list of functions which I've used at this point in the program \n{used_functions}")


