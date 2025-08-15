

""" 
The asterisk in the parameter name *toppings tells Python to make a 
tuple called toppings, containing all the values this function receives

"""

def make_pizza(size, *toppings):
  """"Print the list of topppings that have been requested"""
  #print(toppings)
  
  """Summarize the pizza we are about to make.""" 
  print((f"\nMaking a {size}-inch pizza with the following toppings"))
  for topping in toppings: 
    print(f"- {topping}")





""" 
make_pizza(16, 'pepperoni')
make_pizza(12,'mushroom', 'green peppers', 'extra chesse') """

