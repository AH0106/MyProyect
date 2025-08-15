"""
Python refers to values that cannot change as 
immutable, and an immutable list is called a 

tuple

"""

""" 
For example, if we have a rectangle that should always be a certain size, we 
can ensure that its size doesn’t change by putting the dimensions into a tuple:

We define the tuple 'dimensions', using parentheses instead of square 
brackets

"""

dimensions = (200, 5)
print(dimensions[0])
print(dimensions[1])

#Define a tuple with one item:
my_t = (3,)

""" 
Looping through all valuel in a Tuple
"""

for dimension in dimensions:
  print(dimension)



""" 
Although you can’t modify a tuple, you can assign a new value to a variable 
that represents a tuple. For example, if we wanted to change the dimensions 
of this rectangle, we could redefine the entire tuple:

"""


print("Original dimensions: ")
for dimension in dimensions:
  print(dimension)
  
  
dimensions = (400, 100)
print("\nModified Dimension: ")
for dimension in dimensions:
  print(dimension)