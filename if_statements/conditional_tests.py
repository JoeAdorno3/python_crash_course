# goal of program is to practice conditional tests w/ various examples 

#test using inequality and equality w/ strings
pizza = 'deep dish'
print("I predict pizza != Deep Dish")
print(pizza == 'Deep Dish')

# test for lower method
print("I predict pizza.lower() == deep dish")
print(pizza.lower() == 'deep dish')

# numerical tests
age = 42
print("I predict age != 40")
print(age == 40)
print("I predict age > 30")
print(age > 30)
print("I predict age >= 42")
print(age >= 42)
print("I predict age <= 43")
print(age <= 43)

# testing using and and or
age_0 = 15
age_1 = 20
print("I predict age_0 > 10 and age_1 > 10")
print((age_0 > 10) and (age_1 > 10))
print("I predict age_0 > 10 or age_1 > 21")
print((age_0 > 10) or (age_1 > 21))

# test whetehr is item is in a list
pizza_toppings = ['mushroom', 'pineapple', 'pepperoni']
print("I predict mushrooms are in the pizza_toppings")
print('mushroom' in pizza_toppings)

# test whether item is not in a list
print("I predict ham is not in pizza toppings")
print('ham' not in pizza_toppings)


