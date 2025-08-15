
print("Organizing a List")

cars = ['bmw', 'audi', 'toyota', 'subaru', 'ferrary']
print(cars)


cars.sort()
print(cars)

"""
  The sort() method changes the order of the list permanently
  sort the list in alphabetical order
"""


print("Reverse order")
cars = ['bmw', 'audi', 'toyota', 'subaru', 'ferrary']
cars.sort(reverse = True)
print(cars)



""" 
  sorted() -> present the list in sorted order, but doesn't affect the 
  actual order of the list

"""
cars = ['bmw', 'audi', 'toyota', 'subaru', 'ferrary']
print("Here is the original list")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))


print("\nHere is the original list again: ")
print(cars)


print("\nPrinting a List in Reverse Order")

cars = ['bmw', 'audi', 'toyota', 'subaru', 'ferrary']
print(cars)

cars.reverse()
print(cars)

print("\nLength of a List")

cars = ['bmw', 'audi', 'toyota', 'subaru', 'ferrary']
print(cars)
print(len(cars))