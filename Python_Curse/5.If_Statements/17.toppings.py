

""" requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
  print("Hold the anchovies!") """
  
  
reques_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in reques_toppings:
  print("Adding mushrooms")
if 'pepperoni' in reques_toppings:
  print("Adding pepperoni")
if 'extra cheese' in reques_toppings:
  print("Adding extra cheese")
  
print("\nFinished making your pizza!")




requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
  if requested_topping == 'green peppers':
    print("Sorry, we are out of green peppers right now")
  else:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


requestedToppings = []

if requestedToppings:
  for requestedTopping in requestedToppings:
    print(f"Adding {requestedTopping}.")
  print("\nFinished making your pizza!")
else:
  print("Are you sure you want a plain pizza?")
  
  
  
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for variable in requested_toppings:
  if variable in available_toppings:
    print(f"Adding {variable}.")
  else:
    print(f"Sorry, we don't have {variable}.") # type: ignore
print("\nFinished making your pizza!")