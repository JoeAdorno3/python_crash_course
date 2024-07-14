# goal of program is to create a glossary of python methods or words via a dictionary object, store their names as key's and their definitions as values, and then neatly print the output

glossary = {
	'dictionary': 'Object in python used to store Key-Value pairs. Created by dict1 = {"key": "value"}.',
	'.get()': 'Method for retrieving values from a python dictionary. Can also be given a value to use if their is no value associated with a key/key doesnot exist.',
	'list': 'Object in python used to store collections of objects. Created by using [] like so: list = ["object1", "num1", "etc."].',
	'tuple': 'Object in python used to store collections of objects. Tuples are immutable, they cannot be changed from their order and the values within cannot be removed. Created by tuple = ("object",).',
	'del': 'python method used to delete/remove objects, variables, etc. to delete a value from a list or dictionary call the object using list index or dictionary key name.', 'set()': 'creates a collection which is unordered, unchangeable, and unindexed which does not allow duplicate values', '.title()': 'string method which capitalizes the first letter in each word in the string', '.lower()': 'changes all letters in a string to lower-case', '.items()': 'dictionary method which displays all key value pairs in the dictionary', '.keys()': 'dictionary method which prints all keys in a dictionary.', '.values()': 'method which prints all values in a dictionary.',
}

counter = 0 

for key, value in glossary.items():
	counter += 1
	print(f"\nLine {counter}")
	print(f"Key: {key}")
	print(f"value: {value}")


