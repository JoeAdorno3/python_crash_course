pizza_toppings = []
user_topping = ''


while user_topping != 'quit':
  user_topping = input("please enter a topping that you'd like added. enter 'quit' to stop adding toppings:\n")
  if user_topping != 'quit':
    pizza_toppings.append(user_topping)
    print(f"let's add {user_topping} to your pizza\n")
    
print("\nyour pizza contains:")
for topping in pizza_toppings:
  print(topping)
