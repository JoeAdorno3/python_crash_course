# goal of program is to create a glossary of python methods or words via a dictionary object, store their names as key's and their definitions as values, and then neatly print the output

glossary = {
	'dictionary': 'Object in python used to store Key-Value pairs. Created by dict1 = {"key": "value"}.',
	'.get()': 'Method for retrieving values from a python dictionary. Can also be given a value to use if their is no value associated with a key/key doesnot exist.',
	'list': 'Object in python used to store collections of objects. Created by using [] like so: list = ["object1", "num1", "etc."].',
	'tuple': 'Object in python used to store collections of objects. Tuples are immutable, they cannot be changed from their order and the values within cannot be removed. Created by tuple = ("object",).',
	'del': 'python method used to delete/remove objects, variables, etc. to delete a value from a list or dictionary call the object using list index or dictionary key name.',
}


print("These are some definitions of terms that you've learned so far:")
print(f"\nDictionary:\n{glossary['dictionary']}")	
print(f"\n.get():\n{glossary['.get()']}")	
print(f"\nlist:\n{glossary['list']}")	
print(f"\ntuple:\n{glossary['tuple']}")	
print(f"\ndel:\n{glossary['del']}")

print("\n\nThis list is just some of the things that you've learned so far.")


