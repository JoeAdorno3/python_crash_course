# this is an exercise to write up a list of different pizzas I enjoy in a list and then print the output

pizza_list = ['new york style', 'deep dish', 'tavern style']

for pizza in pizza_list: 
    print(pizza)

for pizza in pizza_list: 
    print(f"I really love eating {pizza} pizza!")

print("\nThere are so many great kinds of pizza!")

friend_pizza = pizza_list[:]

pizza_list.append('neapolitan pizza')

friend_pizza.append('detroit style')

print("My favorite pizzas are:")
for pizza in pizza_list[0:4]: 
    print(pizza)
    
print("My friend's favorite pizzas are:")
for pizza in friend_pizza[0:4]: 
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizza[:len(friend_pizza) + 1]: 
    print(pizza)
